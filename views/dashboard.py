```python
from flask import Blueprint, render_template
from utils.analytics_handler import get_analytics_data

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def show_dashboard():
    data = get_analytics_data()
    return render_template('dashboard.html', data=data)
```