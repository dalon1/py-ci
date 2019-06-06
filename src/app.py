from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    print("Welcome, dannel")

if __name__ == 'main':
    app.run(host='0.0.0.0', port='8082')