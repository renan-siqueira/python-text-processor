import re

from collections import Counter
from langdetect import detect


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


def summarize_text(text):
    sentences = text.split('.')
    summary = '.'.join(sentences[:3])
    return summary


def detect_language(text):
    return detect(text)


def count_words(text):
    return len(text.split())


def count_characters_with_spaces(text):
    return len(text)


def count_characters_without_spaces(text):
    return len(text.replace(" ", ""))


def count_paragraphs(text):
    return len([p for p in text.split("\n\n") if p])
