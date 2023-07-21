import requests
import json

class SynapAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.synap.io/"

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_nfts(self):
        url = f"{self.base_url}nfts"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_nft(self, nft_id):
        url = f"{self.base_url}nfts/{nft_id}"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def update_nft(self, nft_id, data):
        url = f"{self.base_url}nfts/{nft_id}"
        response = requests.patch(url, headers=self.get_headers(), data=json.dumps(data))
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def delete_nft(self, nft_id):
        url = f"{self.base_url}nfts/{nft_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None
