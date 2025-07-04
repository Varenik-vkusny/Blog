from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, validators
from wtforms.validators import Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.length(min=4, max=25)])
    email = EmailField('Электронная почта', [validators.DataRequired(), Email()])
    password = PasswordField('Пароль', [validators.DataRequired(), validators.length(min=6, max=35), validators.EqualTo('confirm', message='Пароли должны совпадать!')])
    confirm = PasswordField('Подтверждение пароля', [validators.DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Электронная почта', [validators.DataRequired(), Email()])
    password = PasswordField('Пароль', [validators.DataRequired(), validators.length(min=6, max=35)])
    remember = BooleanField('Запомнить меня', default=False)


class PostForm(FlaskForm):
    title = StringField('Заголовок', [validators.DataRequired(), validators.length(max=200)])
    content = StringField('Текст', [validators.DataRequired()])

class CommentForm(FlaskForm):
    text = StringField('', [validators.DataRequired(), validators.length(min=1, max=200)])
    submit = SubmitField('', [validators.DataRequired()])