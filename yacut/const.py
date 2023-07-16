import string
from string import ascii_letters, digits

PATTERN = r'^[a-zA-Z\d]{1,16}$'
LABELS = {
    'original': 'url',
    'short': 'custom_id',
}
ALLOWEED_SYMBOLS = string.ascii_letters + string.digits
LEN_OF_SHORT_ID = 6
PATTERN_FOR_GEN_URL = ascii_letters + digits
MAX_LEGHT = 16
MIN_LEGHT = 1