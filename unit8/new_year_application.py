from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/new_year', methods = ["GET"])
def new_year():
    now = datetime.datetime.today()
    NY = datetime.datetime(2021, 1, 1)
    d = NY - now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)

    return f'До нового года: {d.days} дней {hh} часа {mm} мин {ss} сек.'

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
