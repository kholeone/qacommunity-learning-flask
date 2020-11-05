from flask import render_template, redirect, url_for

from application import app, db
from application.models import Lists

@app.route('/')
def index():
    all_task = Lists.query.all()
    return render_template('index.html', all_task=all_task)

@app.route('/add')
def add():
    new_task = Lists(task="New Task")
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

