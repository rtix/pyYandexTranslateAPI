
class YandexTranslateError(Exception):
    def __init__(self, message):
        super(YandexTranslateError, self).__init__(message + '. Visit https://tech.yandex.com/translate/ for details')

class InvalidAPIKeyError(YandexTranslateError):
    def __init__(self, message):
        super(InvalidAPIKeyError, self).__init__(message)

class BlockedAPIKeyError(YandexTranslateError):
    def __init__(self, message):
        super(BlockedAPIKeyError, self).__init__(message)

class DailyLimitExceededError(YandexTranslateError):
    def __init__(self, message):
        super(DailyLimitExceededError, self).__init__(message)

class TextSizeExceededError(YandexTranslateError):
    def __init__(self, message):
        super(TextSizeExceededError, self).__init__(message)

class UntranslatableTextError(YandexTranslateError):
    def __init__(self, message):
        super(UntranslatableTextError, self).__init__(message)

class DirectionNotSupportedError(YandexTranslateError):
    def __init__(self, message):
        super(DirectionNotSupportedError, self).__init__(message)
