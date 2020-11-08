from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError  

from application.models import Lists

class TodoCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_list = Lists.query.all()
        for list in all_list:
            if list.task == field.data:
                raise ValidationError(self.message)

class TodoForm(FlaskForm):
    task = StringField('Task',
                validators=[
                    DataRequired(),
                    TodoCheck(message='Task already exists')
                 ]
             )
    submit = SubmitField('Add Task')

     
