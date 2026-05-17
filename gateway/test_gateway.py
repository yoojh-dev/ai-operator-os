from openai import OpenAI

client = OpenAI(
    api_key="dummy",
    base_url="http://localhost:4000/v1"
)

response = client.chat.completions.create(
    model="coder",
    messages=[
        {
            "role": "user",
            "content": "write fastapi hello world"
        }
    ]
)

print(response.choices[0].message.content)