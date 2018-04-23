from . import db, admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user, login_manager
from . import login_manager
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    this table will handle mostly login
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    pass_secure = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    is_admin = db.Column(db.Boolean)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    

    def __repr__(self):
        return f'User{self.username}'
# class for blogpost

class Post(UserMixin, db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    post = db.Column(db.String)
    image_name = db.Column(db.String)
    image_url = db.Column(db.String)
    timeposted = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return f'Post{self.post}'

class Role(UserMixin, db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    def __repr__(self):
        return f'Post{self.name}'

class Comment(UserMixin, db.Model):
    __tablename__ = "comments"
    id=db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    users = db.relationship('User', backref='author', lazy='dynamic')
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    def __repr__(self):
        return f'Post{self.comment}'

class Subscribers(UserMixin, db.Model):
    __tablename__ = "subscribers"
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'Subscribers{self.email}'

class MyModelView(ModelView):
    def is_accessible(self):
        return False

            

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Subscribers, db.session))