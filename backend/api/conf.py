LIMIT_VALUE: int = 1

REGEX_FOR_USERNAME: str = (
    r'^(?=.{2,150}$)(?![_.-])(?!.*[_.-]{2})[a-zA-Z0-9._(){}-]+(?<![_.(){}-])$'
)

ERROR_MESSAGE_FOR_VALIDATE_REGEX_USERNAME: str = (
    '\u00B7 Имя пользователя не может быть короче 2 символов.\n'
    '\u00B7 Имя пользователя не может содержать буквы, отличные от латиницы.\n'
    '\u00B7 Имя пользователя может содержать следующие символы: ._(){}-'
)

RESERVED_USERNAME_LIST: tuple[str] = (
    'superuser',
    'admin',
    'administrator',
    'moderator',
    'moder',
    'me',
)
