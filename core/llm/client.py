from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000/v1",
    api_key="dummy"  # LiteLLM proxy는 key 체크 안 하면 상관 없음
)


def chat(prompt: str, model: str = "coder") -> str:
    res = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return res.choices[0].message.content