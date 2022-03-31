from flask import render_template, flash, url_for, redirect, request, jsonify, json
from .forms import ToDoForm
from .models import ToDo
from sqlalchemy.exc import DBAPIError
from app import app, db




@app.route('/')
def home_page():
    return render_template ("index.html", title="")

@app.route('/todoform', methods=['GET','POST'])
def view_todoform():
    form = ToDoForm()
    todo_list = ToDo.query.all()
    print(todo_list)
    if form.validate_on_submit():
        try:
            q = ToDo(title=form.title.data, content=form.content.data, complete=True)
            db.session.add(q)
        except DBAPIError as e:
            db.session.rollback()
            flash(e.detail)
        else:
            db.session.commit()
            todo_list = ToDo.query.all()
            return redirect(url_for('view_todoform'))
    else:
        flash(form.errors)
        print(form.errors)
    return render_template("todoform.html", title="", form=form, todo_list=todo_list if todo_list else list())

@app.route("/add", methods=["POST"])
def view_add():
    title = request.form.get("title")
    new_todo = ToDo(title='title')
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("view_todoform"))


@app.route("/update/<int:id>", methods=["POST", "GET"])
def view_update(id):
    todo = ToDo.query.filter_by(id=id).first()
    print(todo)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("view_todoform"))


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def view_delete(id):
    todo = ToDo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("view_todoform"))


