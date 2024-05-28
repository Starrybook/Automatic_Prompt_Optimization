### For gsm8k:

init prompt:

```
I am attempting to have a language model perform a task. The model will receive an instruction prompt and input data, then output its answer along with an explanation. I am currently focused on finding the most suitable instruction prompt using the information provided below:

<goal>The goal is to solve the mathematical problem and provide the final numerical answer.</goal>

Examples:
### Example 1
<input>"3 lions and 2 rhinos escape from the zoo.  If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"</input>
<output>"10"</output>
<explanation>"They had to recover 3+2=<<3+2=5>>5 animals\nSo it took 5*2=<<5*2=10>>10 hours to recover everyone"</explanation>
### Example 2
<input>"Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"</input>
<output>"30"</output>
<explanation>"10 minutes for 5 miles means 10 minutes / 5 miles = <<10/5=2>>2 minutes/mile\n1 hour is 60 minutes so 60 minutes/hour / 2 minutes/mile = 30 miles/hour"</explanation>
### Example 3
<input>"Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"</input>
<output>"45"</output>
<explanation>"First find the number of tadpoles Trent released: 180 tadpoles * .75 = <<180*.75=135>>135 tadpoles\nThen subtract the number he let go from the total number to find the number of tadpoles he keeps: 180 tadpoles - 135 tadpoles = <<180-135=45>>45 tadpoles"</explanation>

<requirement>The instruction prompt should be general, concise, and efficient, meaning that it should enable the model to produce an output close to the real result.</requirement>

<format>
The instruction prompt could be formatted as follows:
<Explain the task to the language model>
Please make sure you meet the following requirements:
<Provide detailed requirements>
1. <Detailed requirement 1>
2. <Additional detailed requirements...>
<Instruct the model to perform the task>
</format>

Now please help me find the most suitable instruction prompt following the steps bellow:
1. Answer the question: What are the most essential elements needed to make an instruction prompt efficient?
2. Explain what I am attempting to achieve.
3. Describe the desired characteristics of the instruction prompt.
3. Answer the question: What do the examples have in common?
4. Answer the question: What do you think can make the instruction prompt more efficient in performing this task?
5. Remember that the instruction prompt should be concise. Now provide me with the most suitable instruction prompt.
```

````
Answer from GPT-4o v1
......
```
<Explain the task to the language model>
You need to solve a given mathematical problem and provide both the final numerical answer and a detailed explanation of your solution.

<Provide detailed requirements>
1. Read and understand the problem statement provided in the input.
2. Perform the necessary calculations step by step.
3. For each calculation step, write down the arithmetic operations and their results.
4. Summarize the final numerical answer clearly at the end.

<Instruct the model to perform the task>
Solve the problem in the input, explaining each step of your calculation, and provide the final numerical answer at the end. Ensure the explanation is clear and detailed.
```
````

````
Answer from GPT-4o v2
......
---
**Instruction Prompt:**

**Task:** Solve the given mathematical problem and provide the final numerical answer along with a detailed explanation of each step.

**Requirements:**
1. Read the input problem carefully.
2. Identify and list the key components of the problem.
3. Perform the necessary calculations step-by-step.
4. Clearly explain each intermediate step and calculation.
5. Provide the final numerical answer.

**Instructions:**
1. Start by restating the problem and breaking it down into components.
2. Perform the calculations needed to solve the problem.
3. Explain each step, including intermediate calculations and how they lead to the solution.
4. Conclude with the final answer and a brief summary of the steps taken.

**Output Format:**
```
<final numerical answer>
<step-by-step explanation>
```

**Example:**
**Input:** "3 lions and 2 rhinos escape from the zoo. If it takes 2 hours to recover each animal, how long did the zoo spend recovering animals?"
**Output:**
```
10
They had to recover 3+2=5 animals. So it took 5*2=10 hours to recover everyone.
```

---
````

```
Answer from GPT-4o v3 - concise
......
---

**Explain the task to the language model:**
You will solve a mathematical problem presented in a natural language.

**Provide detailed requirements:**
1. Calculate the numerical answer.
2. Provide a step-by-step explanation of how you derived the final answer.

**Instruct the model to perform the task:**
Read the input question, compute the necessary calculations, and then give the final numerical answer along with an explanatory breakdown of each step.

---
```

Instruction prompt extracted:

```
You will solve a mathematical problem presented in a natural language.
1. Calculate the numerical answer.
2. Provide a step-by-step explanation of how you derived the final answer.
Read the input question, compute the necessary calculations, and then give the final numerical answer along with an explanatory breakdown of each step.
```

```
v4
1. **Answer the question: What are the most essential elements needed to make an instruction prompt efficient?**

   The most essential elements needed to make an instruction prompt efficient include:
   - **Clarity:** The task should be explained clearly and unambiguously.
   - **Conciseness:** Instructions should be as brief as possible while covering all necessary details.
   - **Specificity:** The prompt should specify the exact task, the format expected for the output, and any additional components required (e.g., an explanation).
   - **Relevance:** Only include information that is directly relevant to completing the task.

2. **Explain what I am attempting to achieve.**

   You are attempting to create an instruction prompt that guides a language model to solve mathematical problems accurately by analyzing the input data and providing a numerical answer along with a step-by-step explanation.

3. **Describe the desired characteristics of the instruction prompt.**

   The desired characteristics of the instruction prompt include:
   - **General applicability:** The prompt should work for a wide range of mathematical problems.
   - **Precision:** The task description should leave no room for misinterpretation.
   - **Efficiency:** The prompt should enable the model to quickly and accurately generate the expected output.
   - **Structured format:** The format should ensure that the model provides both the answer and a detailed explanation.

4. **Answer the question: What do the examples have in common?**

   The examples share the following commonalities:
   - A mathematical problem is presented in the input.
   - The output is a single numerical answer to the problem.
   - An explanation is provided that includes a step-by-step breakdown of the calculations performed to reach the final answer.

5. **Answer the question: What do you think can make the instruction prompt more efficient in performing this task?**

   To make the instruction prompt more efficient, it should:
   - Clearly specify the requirement for both an answer and a detailed explanation.
   - Simplify and streamline the instructions to minimize ambiguity.
   - Directly address the format and structure required in the output.
   - Emphasize clarity and the logical flow of the explanation.

6. **Provide the most suitable instruction prompt.**

   Here is a concise and efficient instruction prompt based on the provided requirements:

   ```
   <Explain the task to the language model>
   Solve the given mathematical problem and provide the final numerical answer.
   
   Please make sure you meet the following requirements:
   1. Clearly state the final numerical answer.
   2. Provide a detailed explanation of the steps taken to solve the problem.
   
   <Instruct the model to perform the task>
   Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand.
   ```
```

Instruction prompt extracted:

```
Solve the given mathematical problem and provide the final numerical answer.
Please make sure you meet the following requirements:
1. Clearly state the final numerical answer.
2. Provide a detailed explanation of the steps taken to solve the problem.
Perform the calculations needed to solve the problem and ensure the answer is precise. Follow a logical sequence in your explanation to make it easy to understand.
```

