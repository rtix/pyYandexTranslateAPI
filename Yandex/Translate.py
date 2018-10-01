import requests

class Translate:

	def __init__(self, api_key):
		'''Initializing object with Yandex.Translate API key

		:param api_key: Your API key
		'''
		self.api_url = 'https://translate.yandex.net/api/{version}/tr.json/'.format(version='1.5')
		self.api_key = api_key

	def set_key(self, api_key):
		'''Method for API key resetting

		:param api_key: Your API key
		'''
		self.api_key = api_key

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
		response = requests.get(self.api_url + 'translate?', data).json()
		if response['code'] == 200:
			return response['text'][0]
		else:
			return response['message']

	def getLangs(self, ui='en'):
		'''Method for getting supported translation directions. Returns dictionary

		:param ui: Language of code's definitions. English by default
		'''
		data = {'key' : self.api_key, 'ui' : ui}
		response = requests.get(self.api_url + 'getLangs?', data).json()
		if response['code'] == 200:
			return response
		else:
			return response['message']

	def detect(self, text, *hint):
		'''Method for detecting language of text. Returns language code in str

		:param text: Text to detect
		:param hint: Optional parameter. List of probable text languages codes
		'''
		data = {'key' : self.api_key, 'text' : text, 'hint' : hint}
		response =  requests.get(self.api_url + 'getLangs?', data).json()
		if response['code'] == 200:
			return response['lang']
		else:
			return response['message']
