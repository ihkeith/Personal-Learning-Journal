from flask import Flask, g, render_template, flash, redirect, url_for
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user, login_required,
                        current_user)

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = '1@(7uerjamquevb&*(4299lLbOiBqQ956710!mnsqLaeRtBn*&'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Do I want to enable Markdown???

# / - Known as the root page, homepage, landing page but will act as
# the Listing route.
@app.route('/')
def index():
    pass


# /entries - Also will act as the Listing route just like /
@app.route('/entries')
def entries():
    pass


# /entries/new - The Create route

# /entries/<id> - The Detail route

# /entries/<id>/edit - The Edit or Update route

# /entries/<id>/delete - Delete route