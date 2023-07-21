```python
from flask import Flask, request, jsonify
from api import underdog, dispatch, synap
from utils import csv_handler, wallet_handler, nft_handler, metadata_handler, analytics_handler, token_gate
from views import dashboard, user_interface, login, game

app = Flask(__name__)

@app.route('/create_list', methods=['POST'])
def create_list():
    data = request.get_json()
    return underdog.create_list(data)

@app.route('/collect_addresses', methods=['POST'])
def collect_addresses():
    data = request.get_json()
    return wallet_handler.collect_addresses(data)

@app.route('/get_nfts', methods=['GET'])
def get_nfts():
    return synap.get_nfts()

@app.route('/update_metadata', methods=['PUT', 'PATCH'])
def update_metadata():
    data = request.get_json()
    return metadata_handler.update_metadata(data)

@app.route('/send_nfts', methods=['POST'])
def send_nfts():
    data = request.get_json()
    return underdog.send_nfts(data)

@app.route('/dashboard', methods=['GET'])
def view_dashboard():
    return dashboard.view()

@app.route('/user_interface', methods=['GET'])
def view_user_interface():
    return user_interface.view()

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        data = request.get_json()
        return login.user_login(data)
    return login.view()

@app.route('/game', methods=['GET'])
def play_game():
    return game.view()

if __name__ == "__main__":
    app.run(debug=True)
```