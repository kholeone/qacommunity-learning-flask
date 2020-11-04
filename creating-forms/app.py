from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')
    date = DateField()
    number = IntegerField('Add Number')
    decimal = DecimalField()
    language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'thank you' + " "  + first_name + " " +  last_name 

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
