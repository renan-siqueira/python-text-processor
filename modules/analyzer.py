from collections import Counter
import re


def word_count(text):
    """Retorna o número total de palavras no texto."""
    words = re.findall(r'\w+', text)
    return len(words)


def word_frequency(text):
    """Retorna um dicionário com a frequência de cada palavra no texto."""
    words = re.findall(r'\w+', text.lower()) # Convertendo para minúsculo para uma contagem insensível a maiúsculas e minúsculas
    return Counter(words)


def find_matches(text, pattern):
    """Retorna todas as correspondências de um padrão regex no texto."""
    return re.findall(pattern, text)
