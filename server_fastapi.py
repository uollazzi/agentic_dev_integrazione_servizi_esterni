import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv

load_dotenv()


class Domanda(BaseModel):
    testo: str


class Risposta(BaseModel):
    testo: str


client = OpenAI(
    api_key=os.environ.get("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/v1",
)

MODEL = "google/gemma-4-26b-a4b-it"

app = FastAPI()


@app.post("/chat")
def chat(domanda: Domanda) -> Risposta:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Sei un assistente simpatico. Rispondi in italiano in modo breve.",
            },
            {"role": "user", "content": domanda.testo},
        ],
    )

    return Risposta(testo=response.choices[0].message.content or "")
