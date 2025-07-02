import openai
client = openai.OpenAI(
    api_key="-",
    # base_url="http://localhost:8080/v1",
    base_url="https://fm.autoai.dev/v1",
)
response = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[
        {"role": "user", "content": "Hello, how are you?"},
    ]
)
print(response)