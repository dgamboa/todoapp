from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://local-admin@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Model for the to do lists
class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    todos = db.relationship('Todo', backref='list', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<TodoList {self.id} {self.name}>'

# Model for the to do items
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}, list {self.list_id}>'

# Function to create a new to do list
@app.route('/todolists/create', methods=['POST'])
def create_todolist():
    error = False
    body = {}
    try:
        list_name = request.get_json()['name']
        list = TodoList(name=list_name)
        db.session.add(list)
        db.session.commit()
        body['id'] = list.id
        body['name'] = list.name
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort (400)
    else:
        return jsonify(body)

# Function to create a new to do item
@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        list_id = request.get_json()['list_id']
        todo = Todo(description=description, completed=False, list_id=list_id)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort (400)
    else:
        return jsonify(body)

# Function to check a to do list as completed
@app.route('/todolists/<list_id>/set-completed', methods=['POST'])
def set_completed_list(list_id):
    try:
        completedList = request.get_json()['completed']
        list = TodoList.query.get(list_id)
        list.completed = completedList
        for todo in list.todos:
            todo.completed = completedList
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

# Function to check a to do item as completed
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

# Function to delete a to do list
@app.route('/todolists/<list_id>', methods=['DELETE'])
def delete_list(list_id):
    try:
        listDelete = TodoList.query.get(list_id)
        db.session.delete(listDelete)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })

# Function to delete a to do item
@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    try:
        toDelete = Todo.query.get(todo_id)
        db.session.delete(toDelete)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })

# Function to display the active to do list
@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html',
    lists=TodoList.query.order_by('id').all(),
    active_list=TodoList.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id').all()
    )

# Home page route
@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))
