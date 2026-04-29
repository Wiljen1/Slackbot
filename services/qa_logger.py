import json
from datetime import datetime

LOG_FILE = "qa_log.json"


def log_event(question, answer, confidence, sources):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(event)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
