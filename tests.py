import unittest
from tests.test_reader import TestReader
from tests.test_analyzer import TestAnalyzer, TestTranslation

# Isso irá carregar todos os testes das classes TestReader e TestAnalyzer
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(TestReader))
suite.addTests(loader.loadTestsFromTestCase(TestAnalyzer))
suite.addTests(loader.loadTestsFromTestCase(TestTranslation))

# Executar os testes
runner = unittest.TextTestRunner()
runner.run(suite)