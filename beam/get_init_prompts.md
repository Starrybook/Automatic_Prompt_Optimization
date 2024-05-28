### For gsm8k



```
I am attempting to have a language model perform a task. The model will receive an instruction prompt and input data, then output its answer along with an explanation. I am currently focused on finding suitable instruction prompts using the information provided below:

The goal is to solve the mathematical problem and provide the final numerical answer.

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

The instruction prompt should be general, concise, and efficient, meaning that it should enable the model to produce an output close to the real result.

Now please provide me with 8 suitable instruction prompts. In your response, please wrap the prompt with <P> and </P>.
8 suitable instruction prompts:
```

gpt-4o

result:

```
Sure, here are six suitable instruction prompts wrapped with <P> and </P>:

<P>Solve the mathematical problem and provide the final numerical answer along with an explanation.</P>

<P>Calculate the answer to the problem, showing your work and reasoning.</P>

<P>Find the numerical solution to the given problem and explain your process.</P>

<P>Determine the final answer to the math problem and illustrate how you arrived at it.</P>

<P>Solve the problem step-by-step and provide the numerical answer with an explanation.</P>

<P>Work through the math problem and present the final result with a detailed explanation.</P>
```

```
Here are 8 suitable instruction prompts:

<P>Solve the following math problem and explain your solution.</P>

<P>Read the problem, compute the answer, and provide a detailed explanation.</P>

<P>Provide the solution to the given math problem along with an explanation of how you arrived at the answer.</P>

<P>Calculate the result of the problem and explain your reasoning step-by-step.</P>

<P>Determine the answer to the mathematical question and illustrate the steps you took to find it.</P>

<P>Solve the math question and describe the process used to reach the final answer.</P>

<P>Find the numerical solution to the problem and explain the methodology used.</P>

<P>Work out the answer to the problem and provide a clear explanation of your calculations.</P>
```



去掉explanation试一试

```
I am attempting to have a language model perform a task. The model will receive an instruction prompt and input data, then output its answer along with an explanation. I am currently focused on finding suitable instruction prompts using the information provided below:

The goal is to solve the mathematical problem and provide the final numerical answer.

Examples:
### Example 1
<input>"3 lions and 2 rhinos escape from the zoo.  If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"</input>
<output>"10"</output>
### Example 2
<input>"Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"</input>
<output>"30"</output>
### Example 3
<input>"Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"</input>
<output>"45"</output>

Now please provide me with 8 suitable instruction prompts. In your response, please wrap the prompt with <P> and </P>.
8 suitable instruction prompts:
```

```
<P>Solve the given mathematical problem and provide a numerical answer.</P>
<P>Calculate the solution to the problem described and provide the answer as a number.</P>
<P>Analyze the problem, perform the necessary calculations, and write the final number as your answer.</P>
<P>Read the problem statement, determine the correct numerical answer, and output it.</P>
<P>Evaluate the given scenario and compute the correct numerical result.</P>
<P>Interpret the problem, calculate the solution, and give the answer in numerical form.</P>
<P>Understand the mathematical problem and provide the precise numerical answer.</P>
<P>Solve for the numerical result and present the final answer clearly.</P>
```

让结果分点列出：

```
I am attempting to have a language model perform a task. The model will receive an instruction prompt and input data, then output its answer along with an explanation. I am currently focused on finding suitable instruction prompts using the information provided below:

The goal is to solve the mathematical problem and provide the final numerical answer.

Examples:
### Example 1
<input>"3 lions and 2 rhinos escape from the zoo.  If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"</input>
<output>"10"</output>
### Example 2
<input>"Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"</input>
<output>"30"</output>
### Example 3
<input>"Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"</input>
<output>"45"</output>

Now please provide me with 4 suitable instruction prompts. In your response, please wrap the prompt with <P> and </P>, and for each prompt, please list every step like "<P>1. Solve the given mathematical problem. 2. Provide a numerical answer. </P>"
4 suitable instruction prompts:
```

```
<P>1. Read the provided mathematical problem carefully.
2. Identify and perform the necessary calculations to solve the problem.
3. Write down the final numerical answer.
4. Provide an explanation of how you arrived at your answer.</P>

<P>1. Understand the mathematical question presented in the input data.
2. Execute the computations required to find the solution.
3. Document the resulting numerical value as the answer.
4. Clarify the steps taken to reach the final answer.</P>

<P>1. Analyze the mathematical problem given in the input.
2. Determine the appropriate mathematical operations needed to resolve the problem.
3. Capture and state the final numerical result.
4. Offer an explanation detailing the reasoning behind your solution.</P>

<P>1. Thoroughly examine the input mathematical problem.
2. Carry out the necessary calculations to determine the solution.
3. Express the solution as a numerical answer.
4. Explain the process and logic used to solve the problem.</P>
```

