from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = [int(s) for s in numbers.split('/') if s.isdigit()]
    return f"Максимальное число: {max(numbers)}"

if __name__ == '__main__':
    app.run()
