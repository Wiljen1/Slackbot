from openai import OpenAI
import os
from pathlib import Path

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def load_instructions():
    instructions_path = Path("config/instructions.txt")
    return instructions_path.read_text(encoding="utf-8")


def build_context(docs):
    if not docs:
        return "No relevant source passages were found."
    return "\n\n".join(docs)


def generate_answer(question, docs):
    instructions = load_instructions()
    context = build_context(docs)

    prompt = f"""{instructions}

Retrieved source text:
{context}

User question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        temperature=0
    )

    return response.output_text.strip()
