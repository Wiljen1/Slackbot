from services.retrieval_v2 import get_documents
from services.llm_runtime import generate_answer
from services.confidence import calculate_confidence
from services.qa_logger import log_event


def answer_question(question):
    docs = get_documents(question)
    answer = generate_answer(question, docs)
    confidence = calculate_confidence(docs)

    response = f"""Answer:
{answer}

Evidence:
{chr(10).join(docs) if docs else 'No supporting documents found'}

Confidence:
{confidence}
"""

    if confidence == "Low":
        response += "\n\n[FLAG_FOR_REVIEW]"

    # log all low + empty cases
    if confidence == "Low" or not docs:
        log_event(question, answer, confidence, docs)

    return response
