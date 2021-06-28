import requests
from requests.auth import HTTPBasicAuth
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

user_data = {
    "admin": "password"
}


@auth.verify_password
def verify(username, password):
    if not(username and password):
        return False
    return user_data.get(username) == password


"""auth_token = "123321"
user_name = "priya"
Base_url = "http://localhost:9696"""

session = requests.session()
response = session.get(Base_url + "/api/v1/todos/",
                       auth=HTTPBasicAuth(user_name, auth_token))
print(response.json)
