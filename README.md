# pyYandexTranslateAPI

Implementation of Yandex.Translate API as a Python library

Usage
=======================

It's very simple to use. There is only one class: Translate. Just import it:
``` python
from Yandex import Translate
```

And use help(Translate) to get clear documentation of its methods:
```
Help on class Translate in module Yandex.Translate:

class Translate(builtins.object)
 |  Translate(api_key)
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |      Initializing object with Yandex.Translate API key
 |
 |      :param api_key: Your API key
 |
 |  detect(self, text, *hint)
 |      Method for detecting language of text. Returns language code in str
 |
 |      :param text: Text to detect
 |      :param hint: Optional parameter. List of probable text languages codes
 |
 |  getLangs(self, ui='en')
 |      Method for getting supported translation directions. Returns dictionary
 |
 |      :param ui: Language of code's definitions. English by default
 |
 |  set_key(self, api_key)
 |      Method for API key resetting
 |
 |      :param api_key: Your API key
 |
 |  translate(self, text, lang_to, lang_from=None)
 |      Method for translating text. Returns str
 |
 |      :param text: Text to translate
 |      :param lang_to: Translation direction
 |      :param lang_from: Optional parameter for specifying the original language
```
