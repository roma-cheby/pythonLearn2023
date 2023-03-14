from flask import Flask

app = Flask(__name__)
storage = dict()

@app.route("/add/<date>/<int:number>")
def add(date, number):
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    global storage
    storage.setdefault(year, {}).setdefault("summary", 0)
    storage.setdefault(year, {}).setdefault(month, {}).setdefault("summary", 0)
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    storage[year]["summary"] += number
    storage[year][month]["summary"] += number
    return f"Запись о расходах добавлена"

@app.route("/calculate/<int:year>")
def calculate_year(year):
    storage.setdefault(year, {}).setdefault("summary", 0)
    return str(storage[year]["summary"])

@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    storage.setdefault(year, {}).setdefault(month, {}).setdefault("summary", 0)
    return str(storage[year][month]["summary"])

if __name__ == '__main__':
    app.run()



