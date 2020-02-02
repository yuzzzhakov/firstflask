import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_mail import Mail, Message
import json
import requests


app = Flask(__name__)
api = Api(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ["MAIL_USERNAME"]
app.config['MAIL_PASSWORD'] = os.environ["MAIL_PASSWORD"]
app.config['MAIL_DEFAULT_SENDER'] = 'vvvvvv@gmail.com'

mail = Mail(app)

TBOT_TOKEN = os.environ["YUZTESTBOT_TOKEN"]

DATA = {'secret_key': 'secret_value'}
JSON_DATA = json.dumps(DATA)


class GetInfo(Resource):
    def post(self):
        json = request.get_json()
        email(json)
        telegram(json)
        return {'got info': json}, 201


def email(json):
    msg = Message('Secret subject', recipients=[json['e-mail']])
    msg.body = JSON_DATA
    mail.send(msg)


def telegram(json):
    url = f'https://api.telegram.org/bot{TBOT_TOKEN}/sendMessage'
    response = requests.post(url, data={
        "chat_id": json['chat_id'],
        "text": JSON_DATA,
    })
    print(response.text)


api.add_resource(GetInfo, '/')

if __name__ == '__main__':
    app.run(debug=True)
