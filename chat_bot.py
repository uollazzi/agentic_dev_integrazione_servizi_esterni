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

# system prompt: istruzioni di sistema per l'LLM
messagges: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": "Sei un assistente simpatico. Rispondi in italiano, in modo conciso e non inserire emoji nel testo.",
    }
]

while True:
    domanda = input("Tu  > ")
    if domanda.strip().lower() == "esci":
        break

    messagges.append({"role": "user", "content": domanda})

    response = client.chat.completions.create(model=MODEL, messages=messagges)
    risposta = response.choices[0].message.content

    messagges.append({"role": "assistant", "content": risposta})
    print(f"Bot > {risposta}")

# contesto: tutte le informazioni che mandiamo all'LLM (storia della chat, documenti) su cui l'LLM si basa per rispondere
