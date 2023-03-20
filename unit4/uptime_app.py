from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/uptime")
def get_uptime():
    command = "uptime"
    UPTIME = str(subprocess.check_output(["wsl", 'uptime']))
    UPTIME = UPTIME[UPTIME.find("up") + 2:UPTIME.find("users") - 5]
    return f"Current uptime is {UPTIME}"

if __name__ == '__main__':
    app.run()