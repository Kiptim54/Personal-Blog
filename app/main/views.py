from . import main
from flask import render_template, url_for , redirect
from flask_login import current_user
from .forms import PostForm
from app.models import Post, User, Role
from .. import db

@main.route('/',methods=['POST','GET'])
def index():
    title= "Personal Blog | Home "
    all = Post.query.all()
    all.reverse()
  
    return render_template('index.html', title = title, posts=all)
    

@main.route('/profile')
def profile():
    title = "Profile"
    # user = User.query.filter_by(username=username).first_or_404()
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
    print(posts)

    return render_template('profile.html' ,posts=posts)

@main.route('/post', methods=['GET', 'POST'])
def post():
    title = "Post Article"
    Blog = PostForm()
    if Blog.validate_on_submit():
        post = Post(post = Blog.Entry.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        print(post)
        return redirect(url_for('main.post'))
    
    all = Post.query.all()
    all.reverse()
    print(all)
        
    

    return render_template('post.html', Post=Blog, title=title, posts=all)
