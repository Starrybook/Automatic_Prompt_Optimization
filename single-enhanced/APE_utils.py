import json
import random
import datetime
import os
from APE_templates import *

from openai import OpenAI
client = OpenAI(
    api_key="",
)

"""
Data processing. 
Shared functions. 
"""
def gen_samples_from_dataset(data_path: str, sample_num: int, keep_orginal_order: bool):
    with open(data_path, 'r') as f:
        data = json.load(f)
    samples = data[:sample_num] if keep_orginal_order else random.sample(data, sample_num)
    return samples

def write_target_model_responses(TARGET_MODEL: str, response_file_dir: str, responses: list):
    if not os.path.exists(response_file_dir):
        os.makedirs(response_file_dir)
    file_name = response_file_dir + f"/res_{TARGET_MODEL}_{datetime.datetime.now().strftime('%m%d_%H%M%S')}.json"
    with open(file_name, 'w') as f:
        json.dump(responses, f, indent=4)
    print(f"Responses saved to {file_name}")
    return file_name


"""
Interact with target model. 
Conponent 1: get target model responses.
Conponent 2: parse target model output and save to file.
Conponent 3: calculate the accuracy of responses. 
"""

def get_target_model_responses(CURRENT_DATASET, TARGET_MODEL, MOVIE_RESPONSES_DIR, GSM8K_RESPONSES_DIR, 
                               eval_set: list, prompt_instruction: str, if_print = False, save2file = True):
    responses = []
    for eval_item in eval_set:
        if CURRENT_DATASET == "movie":
            msgs = [{"role": "user", "content": gen_whole_prompt_from_inst(CURRENT_DATASET, prompt_instruction, eval_item["input"])}]
        elif CURRENT_DATASET == "gsm8k":
            msgs = [{"role": "user", "content": gen_whole_prompt_from_inst(CURRENT_DATASET, prompt_instruction, eval_item["question"])}]
        else:
            print(f"Error: CURRENT_DATASET {CURRENT_DATASET} not supported.")
            return
        completion = client.chat.completions.create(
            model=TARGET_MODEL,
            messages=msgs,
        )
        if if_print:
            print(f"golden: {eval_item['output'] if CURRENT_DATASET == 'movie' else eval_item['answer']}")
            print(completion.choices[0].message.content)
            print('='*50)
        if CURRENT_DATASET == "movie":
            responses.append(merge_golden_and_model_output(CURRENT_DATASET, eval_item["input"], eval_item["output"], completion.choices[0].message.content))
        elif CURRENT_DATASET == "gsm8k":
            responses.append(merge_golden_and_model_output(CURRENT_DATASET, eval_item["question"], eval_item["answer"], completion.choices[0].message.content))
    if save2file:
        file_name = write_target_model_responses(
            TARGET_MODEL,
            MOVIE_RESPONSES_DIR if CURRENT_DATASET == "movie" else GSM8K_RESPONSES_DIR, 
            responses
        )
    return responses, file_name

def evaluation_movie(CURRENT_DATASET, CURRENT_RESPONSES_FILE_PATH):
    assert(CURRENT_DATASET == "movie")
    assert(CURRENT_RESPONSES_FILE_PATH != "")
    with open(CURRENT_RESPONSES_FILE_PATH, "r") as f:
        response = json.load(f)
        correct_num = 0
        for item in response:
            if "Yes" in item["golden"] and "Yes" in item["answer"]:
                correct_num += 1
            elif "No" in item["golden"] and "No" in item["answer"]:
                correct_num += 1
        accuracy = correct_num / len(response)
        print(f"Accuracy: {accuracy}")
        return accuracy

def evaluation_gsm8k(CURRENT_DATASET, CURRENT_RESPONSES_FILE_PATH):
    assert(CURRENT_DATASET == "gsm8k")
    assert(CURRENT_RESPONSES_FILE_PATH != "")
    with open(CURRENT_RESPONSES_FILE_PATH, "r") as f:
        response = json.load(f)
        correct_num = 0
        for item in response:
            try:
                item_answer = item["answer"].replace(" ", "").replace(",", "")
                item_answer = ''.join(filter(lambda x: x.isdigit() or x == '.', item_answer))
                eval_item_golden = eval(item["golden"])
                eval_item_answer = eval(item_answer)
                if type(eval_item_golden) == int:
                    eval_item_answer = int(eval_item_answer)
                if eval_item_golden == eval_item_answer:
                    correct_num += 1
            except:
                print(f"Error in evaluating: {item['golden']} vs {item['answer']}")
        accuracy = correct_num / len(response)
        print(f"Accuracy: {accuracy}")
        return accuracy

"""
Interact with LLM prompt optimizer. 
Conponent 1: get error examples.
Conponent 2: get reflection.
Conponent 3: get refinement. 
"""
def get_error_examples_movie(CURRENT_DATASET, CURRENT_RESPONSES_FILE_PATH, error_sample_num: int):
    # 返回的错例可能少于 error_sample_num
    assert(CURRENT_DATASET == "movie")
    assert(CURRENT_RESPONSES_FILE_PATH != "")
    with open(CURRENT_RESPONSES_FILE_PATH, "r") as f:
        response = json.load(f)
        error_responses = []
        for item in response:
            if "Yes" in item["golden"] and "No" in item["answer"]:
                error_responses.append(item)
            elif "No" in item["golden"] and "Yes" in item["answer"]:
                error_responses.append(item)
        random.shuffle(error_responses)
        error_examples = []
        for i in range(min(error_sample_num, len(error_responses))):
            error_examples.append(
                gen_error_examples(i+1, error_responses[i]["input"], 
                                   error_responses[i]["golden"], 
                                   error_responses[i]["answer"] + "\nExplanation: " + error_responses[i]["explanation"])
            )
        return error_examples

def get_error_examples_gsm8k(CURRENT_DATASET, CURRENT_RESPONSES_FILE_PATH, error_sample_num: int):
    # 返回的错例可能少于 error_sample_num
    assert(CURRENT_DATASET == "gsm8k")
    assert(CURRENT_RESPONSES_FILE_PATH != "")
    with open(CURRENT_RESPONSES_FILE_PATH, "r") as f:
        response = json.load(f)
        error_responses = []
        for item in response:
            try:
                item_answer = item["answer"].replace(" ", "").replace(",", "")
                item_answer = ''.join(filter(lambda x: x.isdigit() or x == '.', item_answer))
                eval_item_golden = eval(item["golden"])
                eval_item_answer = eval(item_answer)
                if type(eval_item_golden) == int:
                    eval_item_answer = int(eval_item_answer)
                if eval_item_golden == eval_item_answer:
                    error_responses.append(item)
            except:
                print(f"Error in get_error_examples_gsm8k: {item['golden']} vs {item['answer']}")
        random.shuffle(error_responses)
        error_examples = []
        for i in range(min(error_sample_num, len(error_responses))):
            error_examples.append(
                gen_error_examples(i+1, error_responses[i]["question"], 
                                   error_responses[i]["golden"] + "\nExplanation: " + error_responses[i]["golden_explanation"],
                                   error_responses[i]["answer"] + "\nExplanation: " + error_responses[i]["explanation"])
            )
        return error_examples

def get_reflection_from_optimizer(OPTIMIZER_MODEL: str, whole_prompt: str) -> str:
    msgs = [{"role": "user", "content": whole_prompt}]
    completion = client.chat.completions.create(
        model=OPTIMIZER_MODEL,
        messages=msgs,
    )
    return parse_feedback_reflection(completion.choices[0].message.content)

def get_refinement_from_optimizer(OPTIMIZER_MODEL: str, whole_prompt: str) -> str:
    msgs = [{"role": "user", "content": whole_prompt}]
    completion = client.chat.completions.create(
        model=OPTIMIZER_MODEL,
        messages=msgs,
    )
    return parse_feedback_refinement(completion.choices[0].message.content)