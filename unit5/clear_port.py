import time
from flask import Flask, request
import shlex, subprocess


def activate_server(port):
    print(f"Activate server on {port} port")
    app = Flask(__name__)
    app.run(port=port)

def check_port(port):
    output = subprocess.Popen(["lsof", "-i", f":{port}"],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_string = output.stdout.read().decode()

    if output_string.count(str(port)) == 0:
        activate_server(port)
    else:
        pid = output_string.split()[10]
        cmd = f"kill -9 {pid}"
        subprocess.run(cmd, shell=True)
        print(f"Kill server on {port} port")
        check_port(port)

if __name__ == '__main__':
    subprocess.Popen(['python3', 'create_server_5000.py']) # запускаю сервер, который будет мешать запуску нашего нового сервера
    time.sleep(2)
    check_port(5000)

