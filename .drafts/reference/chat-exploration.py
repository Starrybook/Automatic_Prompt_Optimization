from openai import OpenAI
# import openai

client = OpenAI(
    # This is the default and can be omitted
    api_key="",
)
# openai.api_key = ""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "system", 
        "content": "You are a helpful assistant."
    },
    {
        "role": "user", 
#         "content": "User Preference: \"Ghostbusters (a.k.a. Ghost Busters) (1984)\", \"Leaving Las Vegas (1995)\",\
#  \"Enchanted April (1992)\", \"Goodfellas (1990)\", \"Babe (1995)\", \"Richard III (1995)\", \"What's Eating Gilbert Grape (1993)\",\
#  \"Piano, The (1993)\", \"Six Degrees of Separation (1993)\"\nUser Unpreference: \"Godfather: Part III, The (1990)\"\n\
# Whether the user will like the target movie \"Double Life of Veronique, The (Double Vie de V\u00c3\u00a9ronique, La) (1991)\"?\
# \n Given the user's preference and unpreference, identify whether the user will like the target movie by answering \"Yes.\" or \"No.\"."
        "content": "This is the natural language version of a problem: \"If $r$ is rational $(r \\neq 0)$ and $x$ is irrational, prove that $rx$ is irrational.\" \
\nTranslate the natural language version statement into a **Lean4** version statement: "
    }
  ]
)

# print(completion.choices[0].message)
print(completion.choices[0].message.content)
print(completion)