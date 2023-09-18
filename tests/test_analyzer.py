import unittest
from modules.analyzer import word_count, word_frequency


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.text = "Hello world! Hello universe!"

    def test_word_count(self):
        self.assertEqual(word_count(self.text), 4)

    def test_word_frequency(self):
        freq = word_frequency(self.text)
        self.assertEqual(freq, {"hello": 2, "world": 1, "universe": 1})


if __name__ == "__main__":
    unittest.main()
