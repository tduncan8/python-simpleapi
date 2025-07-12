from flask import request, jsonify
from Models import Students, session
from flask_restx import Namespace, Resource
v1 = Namespace('v1', description='Version 1 API')

@v1.route('/students')
class StudentsAll(Resource):
    def get(self):
        students = session.query(Students).all()
        return {
            "students": [student.to_dict() for student in students]
        }
@v1.route('/student')
class Student(Resource):
    def post(self):
        data = request.get_json()
        req_first_name = data.get("first_name")
        req_last_name = data.get("last_name")
        req_email = data.get("email")
        new_student = Students(first_name = req_first_name,last_name = req_last_name, email = req_email)
        session.add(new_student)
        session.commit()
        return jsonify("ok") 
