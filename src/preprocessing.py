import re

def clean_ingredients(text):
    """
    Cleans ingredient text by removing special characters
    and converting to lowercase.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z, ]", "", text)
    return text


def tokenize_ingredients(text):
    """
    Splits cleaned ingredient text into tokens.
    """
    return [token.strip() for token in text.split(",") if token.strip()]
