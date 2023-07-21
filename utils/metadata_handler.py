```python
import requests

class MetadataHandler:
    def __init__(self, underdog_api_url):
        self.underdog_api_url = underdog_api_url

    def update_metadata(self, nft_id, metadata):
        url = f"{self.underdog_api_url}/nfts/{nft_id}"
        response = requests.patch(url, json=metadata)
        if response.status_code != 200:
            raise Exception(f"Failed to update metadata for NFT {nft_id}")
        return response.json()

    def get_metadata(self, nft_id):
        url = f"{self.underdog_api_url}/nfts/{nft_id}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to get metadata for NFT {nft_id}")
        return response.json()
```