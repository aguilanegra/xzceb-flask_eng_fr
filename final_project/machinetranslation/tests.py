# tests.py
"""Translation testing module"""
import unittest
import translator
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    """TestTranslations Class"""
    def test_english_to_french(self):
        """Test translation from English to French"""
        french_text = english_to_french('Hi')
        self.assertEqual(french_text,'Bonjour') # Happy path: It should be 'Bonjour'
        error_text = english_to_french('')
        self.assertEqual(error_text,'No string provided') # Sad path #1: Input blank string'

    def test_french_to_english(self):
        """Test translation from French to English"""
        english_text = french_to_english('Bonjour')
        self.assertEqual(english_text,'Hello') #It should be 'Hello'
        error_text = french_to_english('')
        self.assertEqual(error_text,'Aucune chaîne fournie') # Sad path #1: Input blank string'

if __name__ == '__main__':
    unittest.main()
