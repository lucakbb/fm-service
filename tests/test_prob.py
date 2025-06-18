import os
import openai

client = openai.Client(
    api_key=os.environ.get("RC_API_KEY"), base_url=os.environ.get("RC_API_BASE")
)
res = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {
            "content": "Who is Pablo Picasso?", 
            "role": "user",
        }
    ],
    stream=False,
    logprobs=True,
)

for chunk in res:
    if len(chunk.choices) > 0 and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
