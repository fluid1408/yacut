from string import ascii_letters, digits


EMPTY_BODY_MESSAGE = 'Отсутствует тело запроса'
NOT_CORRECT_BODY_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
URL_IS_NECESSARILY_MESSAGE = '\"url\" является обязательным полем!'
NAME_TAKEN_MESSAGE_FIRST_PATH = 'Имя '
NAME_TAKEN_MESSAGE_SECOND_PATH = ' уже занято.'

MAX_LEGHT = 16
MIN_LEGHT = 1

PATTERN = r'^[a-zA-Z\d]{1,16}$'
PATTERN_FOR_GEN_URL = ascii_letters + digits
LABELS = {
    'original': 'url',
    'short': 'custom_id',
}