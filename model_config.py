import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/v1",
)

MODEL = "google/gemma-4-26b-a4b-it"


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Inventa il nome di una pizzeria. Rispondi SOLO con il nome.",
        }
    ],
    temperature=1,
    max_tokens=50,
    reasoning_effort="none",
)

print(response.choices[0].message.content)
