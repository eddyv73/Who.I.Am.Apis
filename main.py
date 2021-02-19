from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
