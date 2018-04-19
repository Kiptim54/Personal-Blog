from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Required, Email, EqualTo
from wtforms import ValidationError
from app.models import Post

class PostForm(FlaskForm):
    Entry= TextAreaField('Post an article', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')