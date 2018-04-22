from flask_mail import Message
from flask import render_template
from .. import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'kiptim54@gmail.com'

    email = Message("Thank you", sender='kiptim54@gmail.com', recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)