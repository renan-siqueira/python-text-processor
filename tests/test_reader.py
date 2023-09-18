import unittest
from modules.reader import read_from_file, write_to_file


class TestReader(unittest.TestCase):

    def setUp(self):
        self.sample_text = "Hello, world!"
        self.sample_file = "tests/sample_text.txt"
        write_to_file(self.sample_file, self.sample_text)
    
    def test_read_from_file(self):
        content = read_from_file(self.sample_file)
        self.assertEqual(content, self.sample_text)

    def tearDown(self):
        with open(self.sample_file, 'w') as file:
            file.truncate() # Limpar o arquivo após os testes


if __name__ == "__main__":
    unittest.main()
