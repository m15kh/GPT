import openai

openai.api_key = "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"

import openai
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, ChatGPT!"}
    ],
    max_tokens=10
)

print(response.choices[0].message.content)

