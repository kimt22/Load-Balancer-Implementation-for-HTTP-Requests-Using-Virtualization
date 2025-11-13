## work load sensitivity

from flask import Flask, render_template_string
import requests

html_template = """
<html>
  <body> 
    <h1>Server Loads</h1>
    <table border="1">
      {% for server in servers %}
      <tr>
        <td>{{ server['name'] }}</td>
        <td>{{ loads[server['name']] }}</td>  
      </tr>
      {% endfor %}
    </table>

    {% if selected %}
      <p>Selected Server: {{ selected }}</p>
    {% else %}
      <p>No server available</p>
    {% endif %}
  </body>
</html>
"""

app = Flask(__name__)

servers = [
    {"ip": "<public ip:port>", "name": "VM11"},    # enter your server's public ip's and port's listening to
    {"ip": "<public ip:port>", "name": "VM12"}
]

@app.route('/')
def load_balance():
    loads = {}
    for server in servers:
        ip = server['ip']
        name = server['name']
        try:
            load = float(requests.get(f'http://{ip}/load').text)
            loads[name] = load 
        except Exception as e:
            print(f"Error retrieving load for {name}: {e}")
            loads[name] = 'Error'

    selected = min(loads, key=loads.get) if loads else None

    return render_template_string(html_template, servers=servers, loads=loads, selected=selected)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
