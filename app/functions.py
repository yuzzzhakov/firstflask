from flask_mail import Message
import requests
from .constants import *
from app import app
from flask_mail import Mail
from flask import abort


mail = Mail(app)


def email(json):
    try:
        msg = Message('Secret subject', recipients=[json['e-mail']])
        msg.body = json_data
        mail.send(msg)
    except:
        app.logger.info('got no e-mail or invalid e-mail')
        abort(401)


def telegram(json):
    try:
        url = f'https://api.telegram.org/bot{TBOT_TOKEN}/sendMessage'
        response = requests.post(url, data={
            "chat_id": json['chat_id'],
            "text": json_data,
        })
    except:
        app.logger.info('got no chat_id or invalid chat_id or impossible to send message')
        abort(401)
