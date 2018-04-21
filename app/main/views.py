from . import main
from flask import render_template, url_for , redirect
from flask_login import current_user, login_required
from .forms import PostForm, CommentForm
from app.models import Post, User, Role,Comment
from .. import db
from datetime import datetime

from flask_admin.contrib.sqla import ModelView


@main.route('/',methods=['POST','GET'])
def index():
    title= "Personal Blog | Home "
    all = Post.query.all()
    all.reverse()
  
    return render_template('index.html', title = title, posts=all)
    

@main.route('/profile/<username>')
@login_required

def profile(username):
    
    user = User.query.filter_by(username = username).first_or_404()
    title = "Profile"       
    return render_template('profile.html' , user=user,title=title)

@main.route('/post', methods=['GET', 'POST'])
def post():
    title = "Post Article"
    Blog = PostForm()
    if Blog.validate_on_submit():
        post = Post( title = Blog.title.data ,post = Blog.Entry.data, author=current_user, timeposted =datetime.utcnow() )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post'))
    
    all = Post.query.all()
    all.reverse()
    print(all)

    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.post'))
    allcomments = Comment.query.all()
    
        
    return render_template('post.html', Post=Blog, title=title, posts=all, comment=Comments, allcomments=allcomments)

@main.route('/post/<id>', methods=['POST','GET'])
def fullpost(id):
    title= f'Posts' 
    post = Post.query.filter_by(id=id).first()
    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, post_id=id)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.fullpost', id=post.id))
    allcomments = Comment.query.all()
    postcomments = Comment.query.filter_by(post_id=id).all()
     

    return render_template('fullpost.html', title=title, post=post, comment=Comments, allcomments=allcomments ,postcomments=postcomments)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


