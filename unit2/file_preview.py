import os
from flask import Flask

app = Flask(__name__)

@app.route("/preview/<int:SIZE>/<path:RELATIVE_PATH>")
def preview(SIZE, RELATIVE_PATH):
    file_name = RELATIVE_PATH.split("/")[-1]
    abs_path = os.path.abspath(file_name)
    print(abs_path)
    file = open(abs_path)
    result_text = file.read(SIZE)
    result_size = len(result_text)

    return f"<b>{abs_path}</b> {result_size}<br>{result_text}"

if __name__ == '__main__':
    app.run()
