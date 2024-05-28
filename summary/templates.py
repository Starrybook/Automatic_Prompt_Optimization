import random

MOVIE_INIT_PROMPT_INST = "" # TODO
MOVIE_RESPONSES_FORMAT_SPEC = ""
MOVIE_EXAMPLE = ""

# GSM8K_INIT_PROMPT_INST = "Solve the given mathematical problem and provide the final numerical answer.\
# Please make sure you meet the following requirements:\
# Clearly state the final numerical answer; \
# Provide a detailed explanation of the steps taken to solve the problem. \
# Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand."

# GSM8K_BEAM_INIT_PROMPTS = [ "1. Solve the given mathematical problem. 2. Provide a numerical answer. ",
#                             "1. Calculate the solution to the problem described. 2. Provide the answer as a number. ",
#                             "1. Analyze the problem. 2. Perform the necessary calculations. 3. Write the final number as your answer. ",
#                             "1. Read the problem statement. 2. determine the correct numerical answer, and output it. ",
#                             "1. Evaluate the given scenario. 2. compute the correct numerical result. ",
#                             "1. Interpret the problem. 2. calculate the solution, and give the answer in numerical form. ",
#                             "1. Understand the mathematical problem. 2. Provide the precise numerical answer. ",
#                             "1. Solve for the numerical result. 2. Present the final answer clearly. ",
#                             "1. Solve the following math problem. 2. Explain your solution. ",
#                             "1. Read the problem. 2. Compute the answer. 3. Provide a detailed explanation. ",
#                             "1. Provide the solution to the given math problem along with an explanation of how you arrived at the answer. ",
#                             "1. Calculate the result of the problem. 2. Explain your reasoning step-by-step. ",
#                             "1. Determine the answer to the mathematical question and illustrate the steps you took to find it. ",
#                             "1. Solve the math question and describe the process used to reach the final answer. ",
#                             "1. Find the numerical solution to the problem. 2. Explain the methodology used. ",
#                             "1. Work out the answer to the problem. 2. Provide a clear explanation of your calculations. "
#                             "1. Solve the mathematical problem. 2. Provide the final numerical answer along with an explanation. ",
#                             "1. Calculate the answer to the problem, showing your work and reasoning. ",
#                             "1. Find the numerical solution to the given problem. 2. explain your process. ",
#                             "1. Determine the final answer to the math problem and illustrate how you arrived at it. ",
#                             "1. Solve the problem step-by-step. 2. provide the numerical answer with an explanation. ",
#                             "1. Work through the math problem and present the final result with a detailed explanation. "]

GSM8K_BEAM_INIT_PROMPTS = [ "1. Read the provided mathematical problem carefully. 2. Identify and perform the necessary calculations to solve the problem. 3. Write down the final numerical answer. 4. Provide an explanation of how you arrived at your answer.",
                            "1. Understand the mathematical question presented in the input data. 2. Execute the computations required to find the solution. 3. Document the resulting numerical value as the answer. 4. Clarify the steps taken to reach the final answer.",
                            "1. Analyze the mathematical problem given in the input. 2. Determine the appropriate mathematical operations needed to resolve the problem. 3. Capture and state the final numerical result. 4. Offer an explanation detailing the reasoning behind your solution.",
                            "1. Thoroughly examine the input mathematical problem. 2. Carry out the necessary calculations to determine the solution. 3. Express the solution as a numerical answer. 4. Explain the process and logic used to solve the problem."]

def get_initial_prompt_insts(CURRENT_DATASET, Beam_size, if_shuffle=False):
    if CURRENT_DATASET == "movie":
        return [] # TODO
    elif CURRENT_DATASET == "gsm8k":
        result = []
        for prompt in GSM8K_BEAM_INIT_PROMPTS:
            result.append({"inst": prompt, "accuracy": 0.0, "responses_path": ""})
        if if_shuffle:
            random.shuffle(result)
        if Beam_size > len(GSM8K_BEAM_INIT_PROMPTS):
            print("Beam size is larger than the number of initial prompts.")
            return result
        return result[:Beam_size]

# towards target model
def gen_whole_prompt_from_inst(CURRENT_DATASET, inst_from_optimizer: str, task_input: str):
    GSM8K_RESPONSES_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\n\
Wrap your final answer with <A> and </A>.\n\
The answer between <A> and </A> tags should be only the numerical value without any additional text.\n\
Wrap your explanation with <E> and </E>."
    # \n<E>First find the number of tadpoles Trent released: 180 tadpoles * .75 = <<180*.75=135>>135 tadpoles\nThen subtract the number he let go from the total number to find the number of tadpoles he keeps: 180 tadpoles - 135 tadpoles = <<180-135=45>>45 tadpoles</E>
    GSM8K_EXAMPLE = "Input: Trent caught 180 tadpoles then let 75% of them go. How many did he keep?\nYour answer: <A>45</A>"
    if CURRENT_DATASET == "movie":
        return '' # TODO
    elif CURRENT_DATASET == "gsm8k":
        # return  inst_from_optimizer +"\n\n" \
        #         + GSM8K_RESPONSES_FORMAT_SPEC + "\n\nHere is an example of the task:\n" \
        #         + GSM8K_EXAMPLE + "\n\nNow please provide your answer to this input:\nInput:\n" \
        #         + task_input + "\nYour answer:\n"
        return  inst_from_optimizer +"\n\n" \
                + GSM8K_RESPONSES_FORMAT_SPEC + "\n\nNow please provide your answer to this input:\nInput: " \
                + task_input + "\nYour answer: "

def gen_fewshot_whole_prompt_from_inst(CURRENT_DATASET, inst_from_optimizer: str, task_input: str, eval_set: list):
    GSM8K_RESPONSES_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\n\
Wrap your final answer with <A> and </A>.\n\
The answer between <A> and </A> tags should be only the numerical value without any additional text.\n\
Wrap your explanation with <E> and </E>."
    assert CURRENT_DATASET == "gsm8k"
    GSM8K_EXAMPLE = ""
    for eval_item in eval_set:
        golden_answer = eval_item["answer"].split("####")[-1].strip()
        golden_explanation = eval_item["answer"].split("####")[0].strip()
        GSM8K_EXAMPLE += "Input: " + eval_item["question"] + "\nYour answer: <E>" + golden_explanation + "</E><A>" + golden_answer + "</A>\n\n"
    return  inst_from_optimizer +"\n\n" \
            + GSM8K_RESPONSES_FORMAT_SPEC + "\n\nHere are several examples of the task:\n" \
            + GSM8K_EXAMPLE + "\nNow please provide your answer to this input:\nInput: " \
            + task_input + "\nYour answer:"

# towards prompt optimizer model
def gen_error_examples(sample_index: int, input: str, correct_answer: str, actual_output: str):
    return f"## Wrong example {sample_index}:\n\
### Input: {input}\n\
### Correct answer and explanation: {correct_answer}\n\
### Wrong output and explanation: {actual_output}"

def gen_reflection(FEEDBACK_REASONS_NUM: int, prompt: str, error_examples: list):
    # REASONS_FORMAT_SPEC = "Please list <REASON_NUM> reasons why the prompt could have gotten these examples wrong.\nWrap each reason with <R> and </R>.\nThe reasons:"
    REASONS_FORMAT_SPEC = "Analyze at which step did the follower make mistakes in each example.\n\
Provide <REASON_NUM> suggestions in total for further breaking down the solution at the failed steps.\n\
Wrap each suggestion with <R> and </R>.\n\
The suggestions:"
    reasons_format_spec_final = REASONS_FORMAT_SPEC.replace("<REASON_NUM>", str(FEEDBACK_REASONS_NUM))
    error_examples_str = "\n\n".join(error_examples)
    return "I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n"\
            + prompt + "\n\nBut this prompt gets the following examples wrong:\n"\
            + error_examples_str\
            + reasons_format_spec_final
        

def gen_refinement(prompt: str, error_examples: list, reasons_feedback: str):
    REFINEMENT_REQUIREMENT_SPEC = "Remember that the instruction prompt should be general and efficient, meaning that it should enable the model to produce an output close to the real result.\n\
Do not include any context-specific content shown in the reasons above. Try to make the prompt help solve more general problems.\n\
You can either modify the existing prompt or add more details to it to guide the model to the correct answer.\n\
You can also include correct examples to help the model understand the task better."
    REFINEMENT_FORMAT_SPEC = "In your response, please wrap the prompt with <P> and </P>."
    # error_examples_str = "\n\n".join(random.sample(error_examples, 2))
    error_examples_str = "\n\n".join(error_examples)
            # + prompt + "\n\nBut this prompt does not perform well and gets the some examples wrong. The possible reasons for these errors are:\n"\
    return "I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n"\
            + prompt + "\n\nBut this prompt does not perform well and gets the some examples wrong. Here is some wrong examples: "\
            + error_examples_str + "\n\nLuckily, there have been some suggestions to eliminate the errors:\n"\
            + reasons_feedback + "\n\nBased on the above information, please write an improved prompt that could fix the problem.\n\n"\
            + REFINEMENT_REQUIREMENT_SPEC + "\n"\
            + REFINEMENT_FORMAT_SPEC + "\nThe improved prompt:\n"



""" ----------------------------- parse --------------------------------- """

def parse_feedback_reflection(feedback: str):
    cutset = feedback.split("<R>")
    reasons = [item.split("</R>")[0].strip() for item in cutset if "</R>" in item]
    result = "\n".join(reasons)
    return result

def parse_feedback_refinement(feedback: str) -> list:
    feedback_cut = feedback.split("<P>")
    feedbacks = [item.split("</P>")[0].strip() for item in feedback_cut if "</P>" in item]
    return feedbacks

def parse_target_model_output(output: str):
    try:
        final_answer = output.split("<A>")[1].split("</A>")[0].strip()
    except:
        print(f"Error in parse_target_model_output: {output}")
        final_answer = "NULL"
    try:
        explanation = output.split("<E>")[1].split("</E>")[0].strip()
    except:
        print(f"Error in parse_target_model_output: {output}")
        explanation = "NULL"
    return final_answer, explanation

def merge_golden_and_model_output(CURRENT_DATASET, original_input: str, golden_answer: str, target_model_output: str):
    target_final_answer, target_explanation = parse_target_model_output(target_model_output)
    if CURRENT_DATASET == "movie":
        return {"input": original_input, "golden": golden_answer, "answer": target_final_answer, "explanation": target_explanation}
    elif CURRENT_DATASET == "gsm8k":
        golden = golden_answer.split("####")[-1].strip()
        golden_explanation = golden_answer.split("####")[0].strip()
        return {"question": original_input, "golden": golden, "golden_explanation": golden_explanation, "answer": target_final_answer, "explanation": target_explanation}