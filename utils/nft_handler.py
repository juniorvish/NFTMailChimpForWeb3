```python
import requests
from .api.underdog import UnderdogAPI
from .api.synap import SynapAPI

class NFThandler:
    def __init__(self):
        self.underdog_api = UnderdogAPI()
        self.synap_api = SynapAPI()

    def get_nfts(self):
        response = self.synap_api.get_nfts()
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def send_nfts(self, wallet_addresses, nft_list):
        response = self.underdog_api.send_nfts(wallet_addresses, nft_list)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def update_metadata(self, nft_id, metadata):
        response = self.underdog_api.update_metadata(nft_id, metadata)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def create_list(self, wallet_addresses):
        response = self.underdog_api.create_list(wallet_addresses)
        if response.status_code == 200:
            return response.json()
        else:
            return None
```