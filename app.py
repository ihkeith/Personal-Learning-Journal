from flask import Flask, render_template, flash, redirect, url_for

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'kjnarnENE&@*#HFNW9ejnfdgjh98u254ih5y&#($&@!jjdn22811839490pszzZfd'


@app.route("/")
def index():
    entries = models.Entry.select().limit(10)
    return render_template('index.html', entries=entries)


@app.route('/entries')
def entries():
    entries = models.Entry.select().limit(10)
    return render_template('index.html', entries=entries)


@app.route("/entries/<int:entry_id>")
def detail(entry_id):
    entry = models.Entry.get(models.Entry.id**entry_id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/new', methods=['GET', 'POST'])
def new():
    """Create a new learning entry"""
    form = forms.NewEntry()
    if form.validate_on_submit():
        flash("New entry added! Keep Learning!")
        models.Entry.create(
            title=form.title.data,
            date=form.date.data,
            time_spent=form.time_spent.data,
            learned=form.learned.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit(entry_id):
    entry = models.Entry.get(models.Entry.id**entry_id)
    # https://dzone.com/articles/flask-101-adding-editing-and-displaying-data
    # this link told me how to prepopluate the form
    form = forms.EditEntry(obj=entry)
    if form.validate_on_submit():
        flash("Entry edited!")
        entry.title = form.title.data
        entry.date = form.date.data
        entry.time_spent = form.time_spent.data
        entry.learned = form.learned.data
        entry.resources = form.resources.data
        entry.save()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form)


@app.route('/entries/<int:entry_id>/delete', methods=['GET', 'POST'])
def delete(entry_id):
    entry = models.Entry.get(models.Entry.id**entry_id)
    entry.delete_instance()
    flash("Entry successfully deleted.")
    return redirect(url_for('index'))


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)