import shlex
import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
client_cards = []

class PythonCode(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])

def run_python_code(code, timeout):
    cmd = f'prlimit --nproc=1:1 python3 -c {code}'
    cmd = shlex.split(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        return "Process kill by timeout"
    return outs.decode() or errs.decode()

@app.route('/python_code', methods = ["POST"])
def python_code():
    form = PythonCode()
    if form.validate_on_submit():
        return str(run_python_code(form.code.data, form.timeout.data))
    return form.errors

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
