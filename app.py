import os
import sqlalchemy
import jsonify
from flask import Flask
from flask_restx import Api
from api.v1 import v1

app = Flask(__name__)
api = Api(app)


api.add_namespace(v1, path='/api/v1')


if __name__ == '__main__':
 app.run(Debug=True)
