import os
from flask import Flask, jsonify, request
app = Flask(__name__)
build = os.environ['FLASK_ENV']


@app.route("/")
def index():
    return jsonify({"name": "python-simpleapi", "version": "1.0", "env": build})
