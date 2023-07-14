import string

PATTERN = r'^[a-zA-Z\d]{1,16}$'
LABELS = {
    'original': 'url',
    'short': 'custom_id',
}
ALLOWEED_SYMBOLS = string.ascii_letters + string.digits
LEN_OF_SHORT_ID = 6