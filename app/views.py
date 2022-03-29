from flask import render_template
from .forms import ToDoForm
from app import app




@app.route('/')
def home_page():
    return render_template ("index.html", title="")

@app.route('/todoform')
def view_todoform():
    form = ToDoForm()

    return render_template("todoform.html", title="", form=form)



