from single.APE_templates import *

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

def merge_goden_and_model_output(original_input: str, goden_answer: str, target_model_output: str):
    global CURRENT_DATASET
    target_final_answer, target_explanation = parse_target_model_output(target_model_output)
    if CURRENT_DATASET == "movie":
        return {"input": original_input, "goden": goden_answer, "answer": target_final_answer, "explanation": target_explanation}
    elif CURRENT_DATASET == "gsm8k":
        """
For the GSM8K dataset, the goden answer hase the following format:
"answer": "Janet sells 16 - 3 - 4 = <<16-3-4=9>>9 duck eggs a day.\nShe makes 9 * 2 = $<<9*2=18>>18 every day at the farmer\u2019s market.\n#### 18"
Extract the final answer after "####" as "goden". 
Extract the text part before "####" as "goden_explanation".
        """
        goden = goden_answer.split("####")[-1].strip()
        goden_explanation = goden_answer.split("####")[0].strip()
        return {"input": original_input, "goden": goden, "goden_explanation": goden_explanation, "answer": target_final_answer, "explanation": target_explanation}