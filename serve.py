from flask import Flask, request
import socket
import subprocess
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_number():
    args = ['python3', 'stress_cpu.py']
    subprocess.Popen(args)
    return socket.gethostname()


@app.route('/', methods=['GET'])
def get_number():
    return socket.gethostname()


# app.add_url_rule('/', 'hello', load_balancer2)

if __name__ == '__main__':
    seed = 0
    # app.debug = True
    # app.host = '0.0.0.0'
    # app.port = 80
    app.run(host='0.0.0.0', port=5000)
