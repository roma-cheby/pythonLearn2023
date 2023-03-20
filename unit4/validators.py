from flask import Flask
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, validators, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError

app = Flask(__name__)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min = 1000000000, max = 9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()

@app.route('/registration', methods = ["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Registration Ok. Email: {email}, phone: {phone}"

    return form.errors, 400

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
