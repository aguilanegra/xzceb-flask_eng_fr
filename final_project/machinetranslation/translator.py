# translator.py
"""Translation module"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate English string to French"""
    if not english_text:
        return 'No string provided'
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate French string to English"""
    if not french_text:
        return 'Aucune chaîne fournie'
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
