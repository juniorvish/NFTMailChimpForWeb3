```python
import requests

class UnderdogAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_list(self, list_data):
        response = requests.post(f"{self.base_url}/lists", json=list_data)
        return response.json()

    def collect_addresses(self, list_id, addresses):
        response = requests.post(f"{self.base_url}/lists/{list_id}/addresses", json=addresses)
        return response.json()

    def get_nfts(self):
        response = requests.get(f"{self.base_url}/nfts")
        return response.json()

    def update_metadata(self, nft_id, metadata):
        response = requests.patch(f"{self.base_url}/nfts/{nft_id}", json=metadata)
        return response.json()

    def send_nfts(self, batch_data):
        response = requests.post(f"{self.base_url}/nfts/batch", json=batch_data)
        return response.json()
```