from flask import Flask, request
import shlex, subprocess
app = Flask(__name__)

@app.route("/ps/", methods = ["GET"])
def get_ps():
    args = request.args.getlist("arg")
    user_cmd = ''.join(str(s) for s in args)
    clean_user_cmd = shlex.quote(user_cmd)
    response = str(subprocess.check_output(["wsl", 'ps', clean_user_cmd]).decode())
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run()