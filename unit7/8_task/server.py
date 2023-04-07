import shlex
import subprocess

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

all_logs = []
app = Flask(__name__)
client_cards = []

@app.route('/post_logs', methods = ["POST"])
def post_logs():
    logs = request.get_data()
    print(logs)
    all_logs.append(logs)

@app.route('/get_logs/<id>', methods = ["GET"])
def get_logs(id):
    return all_logs[int(id)-1]

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
