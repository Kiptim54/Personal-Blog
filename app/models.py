from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    username = db.Column(db.String(225), unique=True)
    email = db.Column(db.String(225), unique=True)

    def __repr__(self):
        return f'User{self.username}'
        