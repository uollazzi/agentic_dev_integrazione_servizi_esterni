import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Persona(BaseModel):
    name: str
    age: int
    city: str


client = OpenAI(
    api_key=os.environ.get("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/v1",
)

MODEL = "google/gemma-4-26b-a4b-it"

messagges: list[ChatCompletionMessageParam] = [
    {"role": "system", "content": "Rispondi in JSON"},
    {
        "role": "user",
        "content": "Estrai i dati con i campi name, age, city: Mario ha 30 anni e vive da sempre comodamente nella città del colosseo",
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messagges,
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "persona", "schema": Persona.model_json_schema()},
    },
)


contenuto = response.choices[0].message.content or ""
persona = Persona.model_validate_json(contenuto)

print(persona.name)
print(persona.age)
print(persona.city)
