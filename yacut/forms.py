from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, ValidationError

from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=16, message='Максимальная длина 16 символов')]
    )
    submit = SubmitField('Добавить')

    def validate_custom_id(form, field):
        if URLMap.query.filter_by(short=field.data).first() is not None:
            raise ValidationError(f'Имя {field.data} уже занято!')
