from flask import Flask
from flask_restplus import Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(
    app=app,
    doc="/",
    default_label="Calculator",
    default="Calculator",
)
CORS(app)

from application import route