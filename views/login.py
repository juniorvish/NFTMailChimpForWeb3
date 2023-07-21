```python
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from utils.wallet_handler import WalletHandler

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

class User(UserMixin):
    def __init__(self, wallet_address):
        self.id = wallet_address

@login_manager.user_loader
def load_user(wallet_address):
    return User(wallet_address)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        wallet_address = request.form['wallet_address']
        if WalletHandler.check_wallet(wallet_address):
            user = User(wallet_address)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Wallet address does not exist!'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```