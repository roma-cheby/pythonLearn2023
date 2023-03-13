from flask import Flask
import random
import datetime
import re

def get_book(file):
    return re.findall("\w+", open(file).read())

app = Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counts = 0
book = get_book("war_and_peace.txt")



@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"

@app.route('/cars')
def cars_route():
    return " ".join([str(s) for s in cars])

@app.route('/cats')
def cats_route():
    return random.choice(cats)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"

@app.route('/get_random_word')
def get_random_word():
    return random.choice(book)

@app.route('/counter')
def get_counts():
    global counts
    counts += 1
    return str(counts - 1)

if __name__ == '__main__':
    app.run()
