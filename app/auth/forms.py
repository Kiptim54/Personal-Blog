from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email= StringField('Email',validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[Required()])
    email = StringField("Email", validators=[Email(), Required()])
    password = PasswordField('Password', validators =[Required(),
    EqualTo("password_confirm", message="Password must match")])
    password_confirm = PasswordField('Confirm Password', validators = [Required()])

    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

