import os
from flask import Flask, request
import subprocess

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode()
    except Exception as e:
        return str(e)

app = Flask(__name__)

@app.route('/run')
def server_api():
    command = request.args.get('command')
    return execute_command(command)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))

