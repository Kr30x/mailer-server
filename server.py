import json
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from waitress import serve
import asyncio
from flask_cors import CORS

from bot import send_message



app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'ggolubev.work@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kreox2005'

mail = Mail(app)
CORS(app)

@app.route('/send-email', methods=['POST', 'OPTIONS'])
def send_email():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'This is an OPTIONS request'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    elif request.method == 'POST':
        name = request.json['name']
        mail = request.json['mail']
        body = request.json['body']
        message = f'New client!\nName: {name}\nMail: {mail}\nMessage: {body}'
        response = send_message(message)
        return response


mod = 'dev'

def main():
    port = 80
    print(f'server up at port {port}')
    if mod == 'dev':
        app.run(host='0.0.0.0', port=61759)
    else:
        serve(app, host='0.0.0.0', port=port, threads=4, channel_timeout=0)

if __name__ == '__main__':
    asyncio.run(main())

