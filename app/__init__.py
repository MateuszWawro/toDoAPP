from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask.json import JSONEncoder
from contextlib import suppress


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\mwawro\\PycharmProjects\\toDoAPP\\todoapp_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'the random string'


db = SQLAlchemy(app)


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        # Optional: convert datetime objects to ISO format
        with suppress(AttributeError):
            return obj.isoformat()
        return dict(obj)


app.json_encoder = MyJSONEncoder


from . import views, models

