import unittest
from translation_manager import TranslationManager

class TestTranslationManager(unittest.TestCase):

    def setUp(self):
        self.tm = TranslationManager( translations_path="resources/sample",
                                      translations_file=None,
                                      active_lang="en"
                                     )
        
    def test_default_language_translation(self):
        self.tm.active_lang = "es"
        result = self.tm.translate("GREETINGS")
        self.assertEqual(result, "Hola, Mundo!")

    def test_variable_interpolation(self):
        self.tm.active_lang = "en"
        result = self.tm.translate("SPECIAL_GREETINGS", name="Pepe")
        self.assertEqual(result, "Hello Pepe!")

    def test_missing_key_returns_placeholder(self):
        self.tm.active_lang = "en"
        result = self.tm.translate("UNKNOWN_KEY")
        self.assertEqual(result, "[UNKNOWN_KEY]")

    def test_missing_language_fallback(self):
        self.tm.active_lang = "fr"  # No hay francés
        result = self.tm.translate("GREETINGS")
        self.assertEqual(result, "[GREETINGS]")

if __name__ == "__main__":
    unittest.main()