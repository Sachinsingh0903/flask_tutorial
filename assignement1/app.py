from flask import Flask
import json

app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hello guys'

DATA_FILE = 'data.json'

@app.route('/api/<name>')
def get_data(name):
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    app.run(debug=True)