import sys
from flask import Flask
from datetime import datetime

app = Flask(__name__)
weekdays_tuple = ("понедельника", "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья")

@app.route("/hello-world/<name>")
def hello_world(name):
    weekday = datetime.today().weekday()
    goodies = 'Хорошей' if weekday in [2,4,5] else "Хорошего"
    weekday = weekdays_tuple[weekday]
    return f"Привет, {name}. {goodies} {weekday}!"

if __name__ == '__main__':
    app.run()
