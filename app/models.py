from . import db


class ToDo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
