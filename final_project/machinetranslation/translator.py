'''
Translator
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

__version__= 1.1
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    authenticator=authenticator,version="2018-05-01")

language_translator.set_service_url(f'{url}')

def english_to_french(english_text):
    '''Translates english text to french'''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''Translates french text to english'''
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']