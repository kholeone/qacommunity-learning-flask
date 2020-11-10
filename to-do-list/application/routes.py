from flask import render_template, redirect, url_for

from application import app, db
from application.models import Todo
from application.forms import TodoForm

@app.route('/')
def index():
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(todo=form.todo.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new todo", form=form)

@app.route('/complete/<int:task_id>')
def complete(todo_id):
    todo_to_update = Todo.query.get(todo_id)
    todo_to_update.complete = True
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/incomplete/<int:task_id>')
def incomplete(todo_id):
    todo_to_update = Todo.query.get(todo_id)
    todo_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    form = TodoForm()
    todo_to_update = Todo.query.get(todo_id)
    if form.validate_on_submit():
        todo_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('index')) 
    return render_template('update.html', form=form)

@app.route('/delete')
def delete():
    todo_to_delete = Todo.query.first()
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
