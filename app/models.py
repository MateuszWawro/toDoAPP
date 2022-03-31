from flask import json
from . import db


class ToDo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)
