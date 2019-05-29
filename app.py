from flask import Flask, g, render_template, flash, redirect, url_for, abort
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

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

# Do I want to enable Markdown???

# / - Known as the root page, homepage, landing page but will act as
# the Listing route.
@app.route('/')
@login_required
def index():
    entries = models.Entry.select().limit(20)
    return render_template('index.html', entryies=entries)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash('Your email or password doesn\'t match', 'error')
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash('Your email or password doesn\'t match', 'error')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out! Come back soon!", "success")
    return redirect(url_for('index'))


# /entries - Also will act as the Listing route just like /
@app.route('/entries')
@login_required
def entries():
    entries = models.Entry.select().limit(20)
    return render_template('index.html', entryies=entries)


# /entries/new - The Create route
@app.route('/entries/new', methods=('GET', 'POST'))
@login_required
def create_new_entry():
    form = forms.NewEntry()
    if form.validate_on_submit():
        flash("New entry created!")
        models.Entry.create(
            title=form.title.data.strip(),
            date=form.date.data,
            time_spent=form.time_spent.data,
            learned=form.learned.data.strip(),
            resources=form.resources.data.strip(),
            user=g.user.id,
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

# /entries/<id> - The Detail route
@app.route('/entries/<int:entry_id>')
@login_required
def view_entry(entry_id):
    post = models.Entry.select().where(models.Entry.id == entry_id)
    if post.count() == 0:
        abort(404)
    return render_template('detail.html', post=post)

# /entries/<id>/edit - The Edit or Update route

# /entries/<id>/delete - Delete route


if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            email='joe.schmoe@email.com',
            password='password',
        )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
