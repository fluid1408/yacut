from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp
from .const import PATTERN


class URLMapForm(FlaskForm):

    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Введена некорректная ссылка')
        ]
    )

    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                regex=PATTERN,
                message='Недопустимые символы. Допустимы только буквы "a-Z" и цифры "0-9"')
        ]
    )

    submit = SubmitField('Создать')