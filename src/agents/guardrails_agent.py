BLOCKED = ["sexo", "sexual", "hackear", "crackear", "pirata", "piratería"]

def is_valid_query(objective: str) -> bool:
    text = objective.lower()
    if any(bad in text for bad in BLOCKED):
        return False
    allowed_keywords = ["front", "back", "devops", "mobile", "program", "data", "software"]
    return any(k in text for k in allowed_keywords)
