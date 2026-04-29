from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_answer(question, docs):
    prompt = f"""
Answer ONLY using the following documents:
{docs}

Question:
{question}

Follow strict rules:
- Do not use outside knowledge
- If not found, say so
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output[0].content[0].text
