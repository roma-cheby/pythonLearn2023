from flask import Flask
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, validators, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError, Optional

app = Flask(__name__)

def number_length(min: int, max: int, message: Optional = ""):
    def _number_length(form: FlaskForm, field: Field):
        if len(str(field.data)) < min or len(str(field.data)) > max or field.data <= 0:
            raise ValidationError(message=message)
    return _number_length

class NumberLength:
    def __init__(self, min: int, max: int, message: Optional = ""):
        self.min = min
        self.max = max
        self.message = message
    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data)) < self.min or len(str(field.data)) > self.max or field.data <= 0:
            raise ValidationError(message=self.message)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10,10), NumberLength(10,10)])
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
