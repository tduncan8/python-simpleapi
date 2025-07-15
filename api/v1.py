from flask import request, jsonify, Flask
from Models import Students, session
from flask_restx import Namespace, Resource, Api, fields
app = Flask(__name__)
api = Api(app)


v1 = Namespace('v1', description='User Version 1 API')
api.add_namespace(v1)

student_model = v1.model('Student', {
    'first_name': fields.String(required=True, description="First name"),
    'last_name': fields.String(required=True, description="Last name"),
    'email': fields.String(required=True, description="Email"),
    })

@v1.route('/students')
class StudentsAll(Resource):
    def get(self):
        students = session.query(Students).all()
        return {
            "students": [student.to_dict() for student in students]
        }
@v1.route('/student')
class StudentCreate(Resource):
    @v1.expect(student_model, validate=True)
    def post(self):
        data = request.get_json()
        req_first_name = data.get("first_name")
        req_last_name = data.get("last_name")
        req_email = data.get("email")
        new_student = Students(first_name = req_first_name,last_name = req_last_name, email = req_email)
        session.add(new_student)
        session.commit()
        return jsonify("ok")
@v1.route('/student/<int:student_id>')
class StudentGet(Resource):
    def get(self, student_id):
        student = Students.by_id(student_id)
        if student:
            return student.to_dict(), 200
        return {"message": "Student not found"}, 404
