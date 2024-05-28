from openai import OpenAI

api_key = "sk-XwOZBCJ4jit3NHayEfC377B876564693B620Bc52C5Fe04Cc"
api_base = "https://api.claude-plus.top/v1"
client = OpenAI(api_key=api_key, base_url=api_base)

completion = client.chat.completions.create(
  model="claude-3-opus-20240229",
  messages=[
    {
        "role": "system", 
        "content": "You are a helpful assistant."
    },
    {
        "role": "user", 
        "content": "How can I register for a claude3 account?"
    }
  ]
)

# print(completion.choices[0].message)
print(completion.choices[0].message.content)