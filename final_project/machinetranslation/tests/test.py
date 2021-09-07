import unittest
import translator 
 
class EnglistToFrenchTranlator(unittest.TestCase):
 
    def main_translator_function(self, text, expected):
        """ Helper function to test translator """
 
        translation = translator.english_to_french(text)
        self.assertEqual(translation, expected)
 
    def test_simple_success_case(self):
        """ Testing a simple translation from English to French """ 
        
        text = "Hello" 
        expected = "Bonjour"
 
        self.main_translator_function(text,expected)
   
    def test_fail_case_no_input(self):
        """ Testing Fail Case with Null Input """
 
        text = None 
        with self.assertRaises(ValueError):
            self.main_translator_function(text,None)

class FrenchToEnglishTranlator(unittest.TestCase):
 
    def main_translator_function(self, text, expected):
        """ Helper function to test translator """
 
        translation = translator.french_to_english(text)
        self.assertEqual(translation, expected)
 
    def test_simple_success_case(self):
        """ Testing a simple translation from English to French """ 
        
        text = "Bonjour" 
        expected = "Hello"
 
        self.main_translator_function(text,expected)
 
    def test_fail_case_no_input(self):
        """ Testing Fail Case with Null Input """
 
        text = None 
        with self.assertRaises(ValueError):
            self.main_translator_function(text,None)
    
unittest.main(exit=False)