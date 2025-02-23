import openai

openai.api_key = "api-key"

import openai
response = openai.chat.completions.create(
    model="gpt-3",
    messages=[
        {"role": "user", "content": "Hello, ChatGPT!"}
    ],
    max_tokens=10
)

print(response.choices[0].message.content)

