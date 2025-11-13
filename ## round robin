## round robin

from flask import Flask, request
import requests

app = Flask(__name__)

# Define servers
servers = ['http://<public ip:port>', 'http://<public ip:port>'] #enter your server's public ip's and ports its listening to.

# Counter to keep track of the next server to use
current_server = 0

@app.route('/')
def balancer():
    global current_server
    selected_server = servers[current_server]
    response = requests.get(selected_server)
    current_server = (current_server + 1) % len(servers)
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)
