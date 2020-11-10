from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError  

from application.models import Todo

class TodoCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_todo = Todo.query.all()
        for todo in all_list:
            if todo.task == field.data:
                raise ValidationError(self.message)

class TodoForm(FlaskForm):
    todo = StringField('Task',
                validators=[
                    DataRequired(),
                    TodoCheck(message='Task already exists')
                 ]
             )
    submit = SubmitField('Add Task')

     
