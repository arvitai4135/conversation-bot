# Placeholder for response_formatter.py
def polish_response(text):
    if not text.endswith("."):
        return text.strip() + "."
    return text.strip()
