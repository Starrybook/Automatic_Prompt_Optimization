""" for template """
MOVIE_INIT_PROMPT_INST = "" # TODO
MOVIE_RESPONSES_FORMAT_SPEC = ""
MOVIE_EXAMPLE = ""

# GSM8K_INIT_PROMPT_INST = "Solve the given mathematical problem and provide the final numerical answer.\n\
# Please make sure you meet the following requirements:\n\
# 1. Clearly state the final numerical answer.\n\
# 2. Provide a detailed explanation of the steps taken to solve the problem.\n\
# Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand."

GSM8K_INIT_PROMPT_INST = "Solve the given mathematical problem and provide the final numerical answer.\
Please make sure you meet the following requirements:\
Clearly state the final numerical answer; \
Provide a detailed explanation of the steps taken to solve the problem. \
Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand."
GSM8K_RESPONSES_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\nWrap your final answer with <A> and </A>.\nWrap your explanation with <E> and </E>."
GSM8K_EXAMPLE = "Input: \nTrent caught 180 tadpoles then let 75% of them go. How many did he keep?\nYour answer: \n<E>First find the number of tadpoles Trent released: 180 tadpoles * .75 = <<180*.75=135>>135 tadpoles\nThen subtract the number he let go from the total number to find the number of tadpoles he keeps: 180 tadpoles - 135 tadpoles = <<180-135=45>>45 tadpoles</E>\n<A>45</A>"

REASONS_FORMAT_SPEC = "Please list <REASON_NUM> reasons why the prompt could have gotten these examples wrong.\nWrap each reason with <R> and </R>.\nThe reasons:"
REFINEMENT_REQUIREMENT_SPEC = "Remember that the instruction prompt should be general and efficient, meaning that it should enable the model to produce an output close to the real result."
# REFINEMENT_FORMAT_SPEC = "The instruction prompt could be formatted as follows (content between braces should be replaced with the appropriate information, then remove the braces):\n\
# {explain the task}\n\
# Please make sure to meet the following requirements:\n\
# {provide detailed requirements bellow}\n\
#     1. {Detailed requirement 1}\n\
#     2. {Additional detailed requirements...}\n\
# {tell the model to perform the task}\n\n\
# In your response, please wrap the prompt with <P> and </P>."
REFINEMENT_FORMAT_SPEC = "In your response, please wrap the prompt with <P> and </P>."

""" for data_process """
MOVIE_100_SAMPLES_PATH = "../data/movie/eval.json"
MOVIE_1000_SAMPLES_PATH = "../data/movie/train.json"
GSM8K_100_SAMPLES_PATH = "../data/gsm8k/eval.json"
GSM8K_1374_SAMPLES_PATH = "../data/gsm8k/test.json"

"""
gsm8k examples:
{
    "question": "3 lions and 2 rhinos escape from the zoo.  If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?", 
    "answer": "They had to recover 3+2=<<3+2=5>>5 animals\nSo it took 5*2=<<5*2=10>>10 hours to recover everyone\n#### 10"
}
{
    "question": "Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?", 
    "answer": "10 minutes for 5 miles means 10 minutes / 5 miles = <<10/5=2>>2 minutes/mile\n1 hour is 60 minutes so 60 minutes/hour / 2 minutes/mile = 30 miles/hour\n#### 30"
}
{
    "question": "Trent caught 180 tadpoles then let 75% of them go. How many did he keep?", 
    "answer": "First find the number of tadpoles Trent released: 180 tadpoles * .75 = <<180*.75=135>>135 tadpoles\nThen subtract the number he let go from the total number to find the number of tadpoles he keeps: 180 tadpoles - 135 tadpoles = <<180-135=45>>45 tadpoles\n#### 45"
}
"""

"""
Templates for APE tasks. 
Explicit reflection. 
-----------------------------------------------------------------------------------------

[[Get response]] :=
  [[prompt_inst]] + '\n\n'
+ [[response_format_spec]] + ''\n\nHere is an example of the task:\n'
+ [[exapmle]] + '\n\nNow please provide your answer to this input:\nInput:\n'
+ [[input]]  + '\nYour answer:\n' ->[target model]-> responses(answer + explanation)

[[Case: gsm8k dataset : prompt_inst]] :=
# initial prompt from gpt-4o
"Solve the given mathematical problem and provide the final numerical answer.
Please make sure you meet the following requirements:
1. Clearly state the final numerical answer.
2. Provide a detailed explanation of the steps taken to solve the problem.
Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand."

[[response_format_spec]] :=
"Your answer should contain both the final answer and an explanation.
Wrap your final answer with <A> and </A>.
Wrap your explanation with <E> and </E>."

[[example]] :=
Input: 
Trent caught 180 tadpoles then let 75% of them go. How many did he keep?
Your answer: 
<E>First find the number of tadpoles Trent released: 180 tadpoles * .75 = <<180*.75=135>>135 tadpoles
Then subtract the number he let go from the total number to find the number of tadpoles he keeps: 180 tadpoles - 135 tadpoles = <<180-135=45>>45 tadpoles</E>
<A>45</A>

-----------------------------------------------------------------------------------------

[[Reflection]] :=
  'I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n'
+ [[prompt_inst]] + '\n\nBut this prompt gets the following examples wrong:\n'
+ [[error_examples]] 
+ [[reasons_format_spec]] ->[optimzer:reflection]-> reasons

[[error_examples]] :=
## Wrong example {sample index}:
### Input: {input}
### Correct answer: {correct answer}
### Output: {actual output}

[[reasons_format_spec]]
Please list 3 reasons why the prompt could have gotten these examples wrong. 
Wrap each reason with <R> and </R>.
The reasons:

-----------------------------------------------------------------------------------------

[[Refinement]] :=
  'I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n'
+ [[prompt_inst]] + '\n\nBut this prompt does not perform well and gets the some examples wrong. The possible reasons for these errors are:\n'
+ [[reasons]] + '\n\nBased on the above information, please write an improved prompt that could fix the problem.\n\n'
+ [[requirement_spec]] + '\n'
+ [[format_spec]] + '\nThe improved prompt:\n'->[optimizer:refinement]-> improved_prompt

[[requirement_spec]]
Remember that the instruction prompt should be general and efficient, meaning that it should enable the model to produce an output close to the real result.

[[format_spec]]
The instruction prompt could be formatted as follows (content between \"/*\" and \"*/\" should be replaced with the appropriate information):
/*explain the task*/
Please make sure to meet the following requirements:
/*provide detailed requirements bellow*/
    1. /*Detailed requirement 1*/
    2. /*Additional detailed requirements...*/
/*tell the model to perform the task*/

In your response, please wrap the prompt with <P> and </P>.

-----------------------------------------------------------------------------------------

"""

# towards target model
def gen_whole_prompt_from_inst(CURRENT_DATASET, inst_from_optimizer: str, task_input: str):
    global GSM8K_RESPONSES_FORMAT_SPEC, GSM8K_EXAMPLE
    if CURRENT_DATASET == "movie":
        return '' # TODO
    elif CURRENT_DATASET == "gsm8k":
        return  inst_from_optimizer +"\n\n" \
                + GSM8K_RESPONSES_FORMAT_SPEC + "\n\nHere is an example of the task:\n" \
                + GSM8K_EXAMPLE + "\n\nNow please provide your answer to this input:\nInput:\n" \
                + task_input + "\nYour answer:\n"

# towards prompt optimizer model
def gen_error_examples(sample_index: int, input: str, correct_answer: str, actual_output: str):
    return f"## Wrong example {sample_index}:\n### Input: {input}\n### Correct answer: {correct_answer}\n### Output: {actual_output}"

def gen_reflection(FEEDBACK_REASONS_NUM: int, prompt: str, error_examples: list):
    global REASONS_FORMAT_SPEC
    reasons_format_spec_final = REASONS_FORMAT_SPEC.replace("<REASON_NUM>", str(FEEDBACK_REASONS_NUM))
    error_examples_str = "\n\n".join(error_examples)
    return "I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n"\
            + prompt + "\n\nBut this prompt gets the following examples wrong:\n"\
            + error_examples_str\
            + reasons_format_spec_final
        

def gen_refinement(FEEDBACK_IMPROVED_PROMPTS_NUM: int, prompt: str, error_examples: list, reasons_feedback: str):
    global REFINEMENT_REQUIREMENT_SPEC, REFINEMENT_FORMAT_SPEC
    # error_examples_str = "\n\n".join(error_examples)
    return "I am attempting to write a instruction prompt to have a language model perform a task.\nMy current prompt is:\n"\
            + prompt + "\n\nBut this prompt does not perform well and gets the some examples wrong. The possible reasons for these errors are:\n"\
            + reasons_feedback + "\n\nBased on the above information, please write an improved prompt that could fix the problem.\n\n"\
            + REFINEMENT_REQUIREMENT_SPEC + "\n"\
            + REFINEMENT_FORMAT_SPEC + "\nThe improved prompt:\n"



"""
Parse the feedback from the LLM prompt optimizers. 
Part 1: Reflection
Reflection prompt format:
<Start>I am trying to write a task prompt.
My current prompt is:
"{prompt to be refined}"
But this prompt gets the following examples wrong:
{error example * n}
Please give 3 reasons why the prompt could have gotten these examples wrong. 
Wrap each reason with <R> and </R>.
The reasons are:
</End>

To parse: extract the content between <R> and </R> tags.

Part 2: Refinement
<Start>I am trying to write a task prompt.
My current prompt is:
"{prompt to be refined}"
But this prompt gets the following examples wrong:
{error example * n}
Based on these examples, the problem with this prompt is that:
{reasons feedback}
Based on the above information, please write 2 different improved prompts that could fix the problem.
Improved prompts should be SLIGHTLY different from the original prompt. 
Wrap each prompt with <P> and </P>.
The improved prompts are:
</End>

To parse: extract the content between <P> and </P> tags.
"""

def parse_feedback_reflection(feedback: str):
    cutset = feedback.split("<R>")
    reasons = [item.split("</R>")[0].strip() for item in cutset if "</R>" in item]
    result = "\n".join(reasons)
    return result

def parse_feedback_refinement(feedback: str) -> list:
    feedback_cut = feedback.split("<P>")
    feedbacks = [item.split("</P>")[0].strip() for item in feedback_cut if "</P>" in item]
    return feedbacks

"""
Parse the output from the target model. 
Prompt format:
[[Instruction in different cases]]
Your answer should contain both the final answer and an explanation.
Wrap your final answer with <A> and </A>.
Wrap your explanation with <E> and </E>.
Please be concise and to the point.

To parse: 
extract the content between <A> and </A> tags as the final answer, 
and the content between <E> and </E> tags as the explanation.
"""

def parse_target_model_output(output: str):
    final_answer = output.split("<A>")[1].split("</A>")[0].strip()
    explanation = output.split("<E>")[1].split("</E>")[0].strip()
    return final_answer, explanation

def merge_golden_and_model_output(CURRENT_DATASET, original_input: str, golden_answer: str, target_model_output: str):
    target_final_answer, target_explanation = parse_target_model_output(target_model_output)
    if CURRENT_DATASET == "movie":
        return {"input": original_input, "golden": golden_answer, "answer": target_final_answer, "explanation": target_explanation}
    elif CURRENT_DATASET == "gsm8k":
        """
For the GSM8K dataset, the golden answer hase the following format:
"answer": "Janet sells 16 - 3 - 4 = <<16-3-4=9>>9 duck eggs a day.\nShe makes 9 * 2 = $<<9*2=18>>18 every day at the farmer\u2019s market.\n#### 18"
Extract the final answer after "####" as "golden". 
Extract the text part before "####" as "golden_explanation".
        """
        golden = golden_answer.split("####")[-1].strip()
        golden_explanation = golden_answer.split("####")[0].strip()
        return {"question": original_input, "golden": golden, "golden_explanation": golden_explanation, "answer": target_final_answer, "explanation": target_explanation}