import openai
client = openai.OpenAI(
    api_key="-",
    # base_url="http://localhost:8080/v1",
    base_url="http://148.187.108.173:8092/v1/service/llm/v1/",
)
response = client.chat.completions.create(
    model="Qwen/Qwen3-32B",
    messages=[
        {"role": "user", "content": "Hello, how are you?"},
    ]
)
print(response)