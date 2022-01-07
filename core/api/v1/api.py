from flask import Blueprint
from flask_restful import Resource, Api

bp_api = Blueprint('apiv1', __name__ )
api = Api(bp_api)

class UserResource(Resource):
    def get(self):
        return {'hello':'world'}
    def post(self):
        return {'hello':'world'}
    def put(self):
        return {'hello':'world'}
    def delete(self):
        return {'hello':'world'}

class HEventResource(Resource):
    def get(self):
        return {'hello':'world'}
    def post(self):
        return {'hello':'world'}
    def put(self):
        return {'hello':'world'}
    def delete(self):
        return {'hello':'world'}

api.add_resource(UserResource, '/user')
api.add_resource(HEventResource, '/event')