from flask import render_template, url_for, redirect, flash,request
from . import auth
from .forms import RegisterForm, LoginForm
from ..models import User
from flask_login import login_user, logout_user
from .. import db
from flask_login import UserMixin

@auth.route('/login',methods=['GET', 'POST'])
def login():
    title = "Login"
    Login = LoginForm()
    if Login.validate_on_submit:
        user = User.query.filter_by( email = Login.email.data).first()
        if user is not None and user.verify_password(Login.password.data):
            login_user(user, Login.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid, Try again')
    return render_template('auth/login.html', Login = Login, ttile=title)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    title= "Register Account"
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=title, form= form)