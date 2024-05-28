""" for template """
# ANSWER_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\nWrap your final answer with <A> and </A>.\nWrap your explanation with <E> and </E>.\nPlease be concise and to the point.\nYour answer:\n"
# remove "Please be concise and to the point."
ANSWER_FORMAT_SPEC = "Your answer should contain both the final answer and an explanation.\nWrap your final answer with <A> and </A>.\nWrap your explanation with <E> and </E>.\nYour answer:\n"
MOVIE_INIT_INST = "Given the user's preference and unpreference, identify whether the user will like the target movie by answering \"Yes.\" or \"No.\"."
GSM8K_INIT_INST = "Please solve the following mathematical problem and provide the final numerical answer."
MOVIE_FORMAT_SPEC = " (Your final answer should be either \"Yes.\" or \"No.\".)"
# GSM8K_FORMAT_SPEC = " (Your final answer should be a numerical value.)"
GSM8K_FORMAT_SPEC = " (Your final answer MUST be only a numerical value like <A>12.5</A> or <A>132</A>.)"

""" for data_process """
MOVIE_100_SAMPLES_PATH = "../data/movie/eval.json"
MOVIE_1000_SAMPLES_PATH = "../data/movie/train.json"
GSM8K_100_SAMPLES_PATH = "../data/gsm8k/eval.json"
GSM8K_1374_SAMPLES_PATH = "../data/gsm8k/test.json"

"""
Templates for APE tasks. 
Explicit reflection. 

[[Initial instruction]] := [[Instruction in different cases]] + [[input]] + [[Answer format specification]]

# 0516: need to add format specification
[[Case 1: movie dataset]] :=
"Given the user's preference and unpreference, identify whether the user will like the target movie by answering \"Yes.\" or \"No.\"."
[[Case 1: format specification]] :=
" (Your final answer should be either \"Yes.\" or \"No.\".)"

[[Case 2: gsm8k dataset]] :=
"Please solve the following mathematical problem and provide the final numerical answer."
[[Case 2: format specification]] :=
" (Your final answer MUST be only a numerical value like <A>12.5</A> or <A>132</A>.)"

[[Answer format specification]] :=
Your answer should contain both the final answer and an explanation.
Wrap your final answer with <A> and </A>.
Wrap your explanation with <E> and </E>.
# Please be concise and to the point.   # 0516: remove this line?
Your answer:

[[Error examples]] :=
### Sample {sample index}
## Input
{input}
## Correct answer
{correct answer}
## Output
{actual output}

[[Reflection]] :=
I am trying to write a task prompt.
My current prompt is:
"{prompt to be refined}"
But this prompt gets the following examples wrong:
{error example * n}
Please give 3 reasons why the prompt could have gotten these examples wrong. 
Wrap each reason with <R> and </R>.
The reasons are:

[[Refinement]] :=
I am trying to write a task prompt.
My current prompt is:
"{prompt to be refined}"
But this prompt gets the following examples wrong:
{error example * n}
Based on these examples, the problem with this prompt is that:
{reasons feedback}
Based on the above information, please write 2 different improved prompts that could fix the problem.
# Improved prompts should be SLIGHTLY different from the original prompt.  # 0516: remove this line?
Wrap each prompt with <P> and </P>.
The improved prompts are:

"""

# towards target model
def gen_init_prompt_movie(task_input: str):
    global MOVIE_INIT_INST, ANSWER_FORMAT_SPEC
    return MOVIE_INIT_INST + MOVIE_FORMAT_SPEC + '\n' + task_input + '\n' + ANSWER_FORMAT_SPEC

def gen_init_prompt_gsm8k(task_input: str):
    global GSM8K_INIT_INST, ANSWER_FORMAT_SPEC
    return GSM8K_INIT_INST + GSM8K_FORMAT_SPEC + '\n' + task_input + '\n' + ANSWER_FORMAT_SPEC

def gen_whole_prompt_from_inst(CURRENT_DATASET, inst_from_optimizer: str, task_input: str):
    global ANSWER_FORMAT_SPEC, MOVIE_FORMAT_SPEC, GSM8K_FORMAT_SPEC
    if CURRENT_DATASET == "movie":
        return inst_from_optimizer + MOVIE_FORMAT_SPEC + '\n' + task_input + '\n' + ANSWER_FORMAT_SPEC
    elif CURRENT_DATASET == "gsm8k":
        return inst_from_optimizer + GSM8K_FORMAT_SPEC + '\n' + task_input + '\n' + ANSWER_FORMAT_SPEC

# towards prompt optimizer model
def gen_error_examples(sample_index: int, input: str, correct_answer: str, actual_output: str):
    return f"### Sample {sample_index}\n## Input\n{input}\n## Correct answer\n{correct_answer}\n## Output\n{actual_output}"

def gen_reflection(FEEDBACK_REASONS_NUM: int, prompt: str, error_examples: list):
    error_examples_str = "\n\n".join(error_examples)
    return f"I am trying to write a task prompt.\nMy current prompt is:\n\"{prompt}\"\nBut this prompt gets the following examples wrong:\n{error_examples_str}\nPlease give {FEEDBACK_REASONS_NUM} reasons why the prompt could have gotten these examples wrong.\nWrap each reason with <R> and </R>.\nThe reasons are:\n"

def gen_refinement(FEEDBACK_IMPROVED_PROMPTS_NUM: int, prompt: str, error_examples: list, reasons_feedback: str):
    error_examples_str = "\n\n".join(error_examples)
    # return f"I am trying to write a task prompt.\nMy current prompt is:\n\"{prompt}\"\nBut this prompt gets the following examples wrong:\n{error_examples_str}\nBased on these examples, the problem with this prompt is that:\n{reasons_feedback}\nBased on the above information, please write {FEEDBACK_IMPROVED_PROMPTS_NUM} different improved prompts that could fix the problem.\nImproved prompts should be SLIGHTLY different from the original prompt.\nWrap each prompt with <P> and </P>.\nThe improved prompts are:\n"
    return f"I am trying to write a task prompt.\nMy current prompt is:\n\"{prompt}\"\nBut this prompt gets the following examples wrong:\n{error_examples_str}\nBased on these examples, the problem with this prompt is that:\n{reasons_feedback}\nBased on the above information, please write {FEEDBACK_IMPROVED_PROMPTS_NUM} different improved prompts that could fix the problem.\nWrap each prompt with <P> and </P>.\nThe improved prompts are:\n"



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
    feedback = feedback.split("<R>")[1].split("</R>")[0].strip()
    return feedback

def parse_feedback_refinement(feedback: str) -> list:
    # feedback = feedback.split("<P>")[1].split("</P>")[0].strip()
    # wrong, there may be mutiple <P> tags
    feedback = feedback.split("<P>")
    feedbacks = [item.split("</P>")[0].strip() for item in feedback if "</P>" in item]
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