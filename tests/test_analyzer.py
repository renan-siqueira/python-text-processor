import unittest
from modules.analyzer import word_count, word_frequency, summarize_text, detect_language


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.text = "Hello world! Hello universe!"

    def test_word_count(self):
        self.assertEqual(word_count(self.text), 4)

    def test_word_frequency(self):
        freq = word_frequency(self.text)
        self.assertEqual(freq, {"hello": 2, "world": 1, "universe": 1})

    def test_summarize_text(self):
        text = "Esta é a primeira frase. Esta é a segunda frase. Esta é a terceira frase. Esta é a quarta frase."
        expected_summary = "Esta é a primeira frase. Esta é a segunda frase. Esta é a terceira frase"
        result = summarize_text(text)
        self.assertEqual(result, expected_summary)
    
    def test_detect_language_english(self):
        text = "This is a simple English text."
        expected_language = "en"
        result = detect_language(text)
        self.assertEqual(result, expected_language)
    
    def test_detect_language_portuguese(self):
        text = "Este é um texto simples em português."
        expected_language = "pt"
        result = detect_language(text)
        self.assertEqual(result, expected_language)


if __name__ == "__main__":
    unittest.main()
