## random 

from flask import Flask, request
import requests
import random

app = Flask(__name__)

servers = [
    {"ip": "http://<public ip:port>", "weight": 7}, # enter your server's public ip's 
    {"ip": "http://<public ip:port>", "weight": 8}
]

weighted_servers = [server["ip"] for server in servers for _ in range(server["weight"])]
current_server_index = 0

@app.route('/')
def balancer():
    selected_server = get_random_server()
    response = forward_request(selected_server)
    return response.content, response.status_code, response.headers.items()

def get_random_server():
    selected_index = random.randint(0, len(weighted_servers) - 1)
    return weighted_servers[selected_index]

def forward_request(selected_server):
    response = requests.get(selected_server + request.full_path)
    return response

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)
