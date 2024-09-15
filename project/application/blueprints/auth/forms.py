from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(max=100)],
        render_kw={"class": "form-control", "placeholder": "Enter username"}
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control", "placeholder": "Enter email"}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Enter password"}
    )
    submit = SubmitField('Register', render_kw={"class": "btn btn-success"})
    

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control", "placeholder": "Enter your email"}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Enter your password"}
    )
    submit = SubmitField('Login', render_kw={"class": "btn btn-success"})
