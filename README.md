# GPT API Script

A simple Python script for interacting with OpenAI's GPT-4o model via API.

## Requirements

- Python 3.6+ 
- OpenAI Python package

## Installation

1. Clone this repository
2. Install required packages:
```
pip install openai
```

## Setup

Replace the placeholder API key in `gpt.py` with your actual OpenAI API key:

```python
openai.api_key = "your-api-key-here"
```

You can get an API key by signing up at [OpenAI's platform](https://platform.openai.com/).

## Usage

Run the script:

```bash
python gpt.py
```

The script currently sends a simple "Hello, ChatGPT!" message to the GPT-4o model and prints the response.

## Customization

You can modify the following parameters in the script:
- Change the model (e.g., "gpt-3.5-turbo", "gpt-4")
- Adjust the message content
- Modify max_tokens to control response length
- Add more parameters like temperature, top_p, etc.

## Example

```python
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms"}
    ],
    max_tokens=100
)
```
