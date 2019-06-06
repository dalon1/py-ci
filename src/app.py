from flask import Flask
from flask import jsonify
from model import Model
from mydb import MyDb

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

@app.route('/firebase')
def get_firebase_db():
    db = MyDb
    return db.get_user('jeHVBG0Uq6nzDbDrS0dy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8082')