from . import main
from flask import render_template

@main.route('/')
def index():
    title= "Personal Blog | Home "

    return render_template('index.html', title = title)

