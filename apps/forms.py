from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


# ログインフォーム
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=100)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=100)])


# ユーザー登録フォーム
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=100)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=100)])
