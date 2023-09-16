def remove_punctuation(text):
    """Remove pontuações do texto."""
    import string
    return text.translate(str.maketrans('', '', string.punctuation))


def replace_text(text, target, replacement):
    """Substitui 'target' por 'replacement' no texto."""
    return text.replace(target, replacement)


def to_uppercase(text):
    """Converte todo o texto para maiúsculas."""
    return text.upper()


def to_lowercase(text):
    """Converte todo o texto para minúsculas."""
    return text.lower()
