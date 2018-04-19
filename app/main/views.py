from . import main
from flask import render_template, url_for , redirect
from flask_login import current_user
from .forms import PostForm
from app.models import Post, User, Role
from .. import db

@main.route('/',methods=['POST','GET'])
def index():
    title= "Personal Blog | Home "
    Blog = PostForm()
    if Blog.validate_on_submit():
        post = Post(post = Blog.Entry.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]
    return render_template('index.html', title = title ,posts=posts, Post=Blog)

@main.route('/profile')
def profile():
    title = "Profile"
    # user = User.query.filter_by(username=username).first_or_404()

    return render_template('profile.html')

