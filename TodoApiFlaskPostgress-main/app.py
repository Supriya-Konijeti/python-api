# app.py
# Purpose: Create a Flask app and define the necessary API routes

from flask import Flask, render_template, request, jsonify
from requests import auth
import requests
from requests.auth import HTTPBasicAuth
from functools import wraps
from flask_restful import Resource, Api
import db

app = Flask(__name__)


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return 'Could not verify your login'
    return decorated


@app.route('/')
def main_page():
    return render_template('home.html')


@app.route('/api/v1/todo', methods=['POST'])
@auth_required
def create_todo():
    request_data = request.get_json()
    new_todo = {
        'id': request_data['id'],
        'name': request_data['name'],
        'company': request_data['company']
    }
    db.insert_into(new_todo)
    return jsonify(new_todo)


@app.route('/api/v1/todos')
@auth_required
def get_todos():
    return jsonify({'todos': db.get_all()})


# Running on port number
app.run(port=9696)
