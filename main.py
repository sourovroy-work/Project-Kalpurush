import os, json
from src import matcher
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Welcome to your Project Kalpurush!!!")

@app.route('/match/<word>', methods=['GET'])
def get_match(word):
    result = []
    for file in get_all_database_files():
        result.extend(matcher.get_match(file, word))
    return json.dumps(list(set(result)))

@app.route('/all', methods=['GET'])
def get_all():
    result = []
    for file in get_all_database_files():
        result.extend(matcher.get_all(file))
    return json.dumps(list(set(result)))


def get_all_database_files():
    files = []
    for file in os.listdir("database"):
        if file.endswith(".txt"):
            files.append(os.path.join("database", file))
    return files


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
