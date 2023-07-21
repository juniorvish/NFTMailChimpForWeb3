```python
from flask import Flask, render_template, request, session
from ..utils.token_gate import check_tokens

app = Flask(__name__)

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'wallet_address' not in session:
        return redirect(url_for('login'))

    wallet_address = session['wallet_address']
    token_count = check_tokens(wallet_address)

    if request.method == 'POST':
        # Assuming the game gives points based on some user action
        points = request.form.get('points')
        # Add points to user's profile
        # This is a placeholder, replace with actual function to update user profile
        update_user_profile(wallet_address, points)

    return render_template('game.html', token_count=token_count)

def update_user_profile(wallet_address, points):
    # Placeholder function to update user profile with earned points
    # Replace with actual implementation
    pass
```