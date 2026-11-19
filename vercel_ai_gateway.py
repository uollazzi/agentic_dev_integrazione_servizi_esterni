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

messagges: list[ChatCompletionMessageParam] = [
    {"role": "system", "content": "Rispondi in italiano, in modo conciso."},
    {"role": "user", "content": "Perchè il cielo è blu?"},
]


# Print della risposta completa (asptta a scrivere fino a che non ha ricevuto tutto il testo)
# response = client.chat.completions.create(model=MODEL, messages=messagges)
# print(response.choices[0].message.content)

# Print della risposta in streaming
stream = client.chat.completions.create(model=MODEL, messages=messagges, stream=True)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

# Utilizzo Tokens
# print(response.usage)
