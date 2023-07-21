import requests
import json

class DispatchAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_message(self, message, wallet_addresses):
        url = f"{self.base_url}/message"
        headers = {'Content-Type': 'application/json'}
        data = {
            "message": message,
            "wallet_addresses": wallet_addresses
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def update_metadata(self, metadata, wallet_address):
        url = f"{self.base_url}/metadata"
        headers = {'Content-Type': 'application/json'}
        data = {
            "metadata": metadata,
            "wallet_address": wallet_address
        }
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        return response.json()

    def get_notifications(self, wallet_address):
        url = f"{self.base_url}/notifications/{wallet_address}"
        response = requests.get(url)
        return response.json()