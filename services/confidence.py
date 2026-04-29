def calculate_confidence(docs):
    if not docs:
        return "Low"
    if len(docs) > 1:
        return "High"
    return "Medium"
