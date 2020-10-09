from app import app
from flask import render_template, request, redirect, url_for
from app.models import TodoItem
from app import db

@app.route('/')
def home():
    incomplete = TodoItem.query.filter_by(complete=False).all()
    complete = TodoItem.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
    todo = TodoItem(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/complete/<id>')
def complete(id):
    todo = TodoItem.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('home'))