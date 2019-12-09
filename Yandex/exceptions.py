
class YandexTranslateError(Exception):
    def __init__(self, message):
        super().__init__(message + '. Visit https://tech.yandex.com/translate/ for details')

class InvalidAPIKeyError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)

class BlockedAPIKeyError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)

class DailyLimitExceededError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)

class TextSizeExceededError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)

class UntranslatableTextError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)

class DirectionNotSupportedError(YandexTranslateError):
    def __init__(self, message):
        super().__init__(message)
