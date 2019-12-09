import requests

from Yandex.exceptions import *


class Translate:

	def __init__(self, api_key):
		'''Initializing object with Yandex.Translate API key

		:param api_key: Your API key
		'''
		self.api_url = 'https://translate.yandex.net/api/{version}/tr.json/'.format(version='v1.5')
		self.api_key = api_key

	def set_key(self, api_key):
		'''Method for API key resetting

		:param api_key: Your API key
		'''
		self.api_key = api_key

	def __raise_exception(self, code, message):
		bad_response_codes = {
			401 : InvalidAPIKeyError,
			402 : BlockedAPIKeyError,
			404 : DailyLimitExceededError,
			413 : TextSizeExceededError,
			422 : UntranslatableTextError,
			501 : DirectionNotSupportedError}
		
		if code in bad_response_codes.keys():
			raise bad_response_codes[code](message)
		else:
			raise YandexTranslateError(message)

	def translate(self, text, lang_to, lang_from = None):
		'''Method for translating text. Returns str

		:param text: Text to translate
		:param lang_to: Translation direction
		:param lang_from: Optional parameter for specifying the original language
		'''
		data = {'key' : self.api_key, 'text' : text, 'lang' : None}
		if lang_from:
			data['lang'] = '{}-{}'.format(lang_from, lang_to)
		else:
			data['lang'] = lang_to
		response = requests.get(self.api_url + 'translate?', data)
		if response.status_code == 200:
			return response.json()['text'][0]
		else:
			self.__raise_exception(response.json()['code'], response.json()['message'])

	def get_langs(self, ui = None):
		'''Method for getting supported translation directions. Returns dictionary

		:param ui: Optional parameter for language of code's definitions
		'''
		data = {'key' : self.api_key, 'ui' : ui}
		response = requests.get(self.api_url + 'getLangs?', data)
		if response.status_code == 200:
			return response.json()
		else:
			self.__raise_exception(response.status_code, response.json()['message'])

	def detect(self, text, *hint):
		'''Method for detecting language of text. Returns language code in str

		:param text: Text to detect
		:param hint: Optional parameter. List of probable text languages codes
		'''
		data = {'key' : self.api_key, 'text' : text, 'hint' : hint}
		response =  requests.get(self.api_url + 'detect?', data)
		if response.status_code == 200:
			return response.json()['lang']
		else:
			self.__raise_exception(response.status_code, response.json()['message'])
