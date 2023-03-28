import shlex
import subprocess

from flask import Flask, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route('/endpoint_1', methods = ["GET"])
def endpoint_1():
    return "endpoint_1"

@app.route('/endpoint_2', methods = ["GET"])
def endpoint_2():
    return "endpoint_2"

@app.errorhandler(404)
def errorhandler(e):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(f'<a href="{url}">{rule.endpoint}</a>')
    return '\n'.join([s for s in links])
if __name__ == '__main__':
    app.run()
