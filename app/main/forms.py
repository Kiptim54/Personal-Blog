from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Required, Email, EqualTo
from wtforms import ValidationError
from app.models import Post, Comment, Subscribers
from flask_wtf.file import FileRequired, file_allowed, FileField

class PostForm(FlaskForm):
    image = FileField("Image", validators=[FileRequired(), file_allowed(images)])
    title = StringField('Title', validators=[DataRequired(),Length(min=1, max=1000)])
    Entry= TextAreaField('Post an article', validators=[DataRequired(), Length(min=1, max=100000000000)])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', [DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Comment')

class SubscribersForm(FlaskForm):
    email = StringField('Subscribe to get alerts', validators=[DataRequired(), Email(), Length(min=1, max=200)])
    submit = SubmitField("Submit")