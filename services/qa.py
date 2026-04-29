from services.retrieval import get_documents
from services.llm import generate_answer
from services.confidence import calculate_confidence


def answer_question(question):
    docs = get_documents(question)
    answer = generate_answer(question, docs)
    confidence = calculate_confidence(docs)

    response = f"""
Answer:
{answer}

Evidence:
{docs}

Confidence:
{confidence}
"""

    if confidence == "Low":
        response += "\n[FLAG_FOR_REVIEW]"

    return response
