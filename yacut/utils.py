import random
import string

from http import HTTPStatus

from .error_handlers import InvalidAPIUsage
from .models import URLMap


def get_unique_short_id():
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )


def validate_custom_id(custom_id):
    if len(custom_id) > 16:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            status_code=HTTPStatus.BAD_REQUEST
        )
    if not (custom_id.isascii() and custom_id.isalnum()):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            status_code=HTTPStatus.BAD_REQUEST
        )
    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(
            f'Имя "{custom_id}" уже занято.',
            status_code=HTTPStatus.BAD_REQUEST
        )
