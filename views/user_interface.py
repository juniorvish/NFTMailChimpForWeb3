```python
from flask import Flask, render_template, request, redirect, url_for
from utils.wallet_handler import WalletHandler
from utils.nft_handler import NftHandler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wallets', methods=['GET', 'POST'])
def wallets():
    if request.method == 'POST':
        wallet_address = request.form.get('wallet_address')
        WalletHandler.add_wallet(wallet_address)
        return redirect(url_for('wallets'))

    wallets = WalletHandler.get_wallets()
    return render_template('wallets.html', wallets=wallets)

@app.route('/nfts', methods=['GET'])
def nfts():
    nfts = NftHandler.get_nfts()
    return render_template('nfts.html', nfts=nfts)

@app.route('/nft/<nft_id>', methods=['GET', 'POST'])
def nft(nft_id):
    if request.method == 'POST':
        metadata = request.form.get('metadata')
        NftHandler.update_metadata(nft_id, metadata)
        return redirect(url_for('nft', nft_id=nft_id))

    nft = NftHandler.get_nft(nft_id)
    return render_template('nft.html', nft=nft)

@app.route('/send_nfts', methods=['POST'])
def send_nfts():
    nft_ids = request.form.getlist('nft_ids')
    wallet_addresses = request.form.getlist('wallet_addresses')
    NftHandler.send_nfts(nft_ids, wallet_addresses)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```