import flask
# from flask import request

app = flask. Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'
