from app import app
from flask import render_template
from app.models import TodoItem
from app import db

@app.route('/')
def home():
    incomplete = TodoItem.query.filter_by(complete=False).all()
    complete = TodoItem.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)gi
