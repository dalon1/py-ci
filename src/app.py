from flask import Flask
from flask import jsonify
from model import Model

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome, dannel"

@app.route('/welcome/<name>')
def welcome_name(name):
    return "Welcome, " + name

@app.route('/user')
def get_user():
    user = Model
    return jsonify(user.get_user())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8082')