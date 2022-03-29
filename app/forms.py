from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

class ToDoForm(FlaskForm):
    title = StringField('Tytuł', validators=[validators.Length(min=3, max=20)])
    content = TextAreaField('Treść')
    submit = SubmitField ('Wyślij')



