import jsonify
from Models import Students, session
from flask_restx import Namespace, Resource
v1 = Namespace('v1', description='Version 1 API')

@v1.route('/students')
class StudentsAll(Resource):
    def get(self):
        students = session.query(Students).all()
        return jsonify(students)

