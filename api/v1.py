from flask_restx import Namespace, Resource

v1 = Namespace('v1', description='Version 1 API')

@v1.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

