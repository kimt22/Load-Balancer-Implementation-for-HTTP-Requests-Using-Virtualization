## weighted round robin

from flask import Flask, request
import requests

app = Flask(__name__)

servers = [
    {"ip": "http://<public ip:port>", "weight": 7},   #enter your server's public ip's and ports its listening to.
    {"ip": "http://<public ip:port>", "weight": 8}
]

weighted_servers = [server["ip"] for server in servers for _ in range(server["weight"])]
current_server_index = 0

@app.route('/')
def balancer():
    global current_server_index
    selected_server = get_next_server()
    response = forward_request(selected_server)
    return response.content, response.status_code, response.headers.items()

def get_next_server():
    global current_server_index
    selected_server = weighted_servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(weighted_servers)
    return selected_server

def forward_request(selected_server):
    response = requests.get(selected_server + request.full_path)
    return response

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)
