from flask import render_template, redirect, url_for

from application import app, db
from application.models import Lists
from application.forms import TodoForm

@app.route('/')
def index():
    all_task = Lists.query.all()
    return render_template('index.html', all_task=all_task)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_task = Lists(task=form.task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new todo", form=form)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task_to_update = Lists.query.get(task_id)
    task_to_update.complete = True
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/incomplete/<int:task_id>')
def incomplete(task_id):
    task_to_update = Lists.query.get(task_id)
    task_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<task>')
def update(task):
    task_to_update = Lists.query.first()
    task_to_update.task = task
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/delete')
def delete():
    task_to_delete = Lists.query.first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
