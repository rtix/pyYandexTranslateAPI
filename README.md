# pyYandexTranslateAPI
Implementation of Yandex.Translate API as a Python library

# Get pyYandexTranslateAPI
```
pip install pyyandextranslateapi
```

# Usage
It's very simple to use. There is only one class: Translate

## Import
``` python
from Yandex import Translate
```

## Initialize
Initialize your Translate with your API key for Yandex.Translate.
You can get it for free on https://translate.yandex.com/developers/keys.
``` python
t = Translate(api_key=API_KEY)
```
Just in case, you can change your key any moment:
``` python
t.set_key(OTHER_API_KEY)
```

## Use it
### Get list of supported languages
``` python
t.get_langs()
# {'af': 'Afrikaans', 'am': 'Amharic', 'ar': 'Arabic', ...}
```
There is an optional parameter `ui` here which is for language of definitions of language codes:
``` python
t.get_langs(ui='ru')
# {'af': 'Африкаанс', 'am': 'Амхарский', 'ar': 'Арабский', ...}
```

### Detect the language of text
``` python
t.detect(text='Здравствуйте!')
# ru
```
There is an optional parameter `hint` where you can pass list of hints, if you have suggestions about text language:
``` python
t.detect('Здравствуйте!', hint=['ru', 'tt'])
# ru
```
But it's not the list from where API will choose language! API can ingore your hints if he thinks that you are wrong:
``` python
t.detect('Hello!', ['ru', 'tt'])
# en
```

### Translate text
``` python
t.translate(text='Hello!', lang_to='ru')
# Здравствуйте!
```
There is an optional parameter `lang_from` where you can pass language of original text:
``` python
t.translate('Hello!', 'ru', lang_from='en')
# Здравствуйте!
```

## For more information
### About API
https://tech.yandex.com/translate/doc/dg/concepts/about-docpage/

### About this library
radif.tazetdinov@mail.ru
