import datetime
from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse
from core.models import db, User
from core.helper import is_email, user_data_control

bp_api = Blueprint('apiv1', __name__ )
api = Api(bp_api)
parser = None

class UserResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_name", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("user_email", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("user_password", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("new_user_password", type=str, required=False, location=("json", "values"))
        self.parser.add_argument("new_user_name", type=str, required=False, location=("json", "values"))
    def get(self):
        return jsonify(message="Please read the usage information on the home page.") 
    def post(self):
        data = self.parser.parse_args()
        data, ok = user_data_control(data)
        if not ok:
            return jsonify(message=data)
        try:
            if User.query.filter_by(username=data['user_name']).first() is not None or User.query.filter_by(email=data['user_email']).first() is not None:
                return jsonify(message="The username or e-mail is already registered in the system.")
            u = User(username=data['user_name'], email=data['user_email'], password=data['user_password'])
            db.session.add(u)
            db.session.commit()
            return jsonify(message="The user has been successfully registered.")
        except Exception as e:
            print(str(e))
            return jsonify(message="Failed to register user. This may be due to the parameters you sent. If the problem still persists, contact us.")

    def put(self):
        data = self.parser.parse_args()
        data, ok = user_data_control(data)
        if not ok:
            return jsonify(message=data)
        new_data, ok = user_data_control({"user_email":data['user_email'], "user_name":data['new_user_name'], "user_password":data['new_user_password']})
        if not ok:
            return jsonify(message=new_data)
        try:
            u = User.query.filter_by(username=data['user_name'], email=data['user_email'], password=data['user_password']).first()
            if u is None:
                return jsonify(message="User not found.")
            u.username = data['new_user_name']
            u.password = data["new_user_password"]
            db.session.commit()
            return jsonify(message="The user has been successfully deleted.")
        except Exception as e:
            print(str(e))
            return jsonify(message="The user could not be deleted. This could be due to the parameters you sent. If the problem still persists, contact us.")

    def delete(self):
        data = self.parser.parse_args()
        data, ok = user_data_control(data)
        if not ok:
            return jsonify(message=data)
        try:
            u = User.query.filter_by(username=data['user_name'], email=data['user_email'], password=data['user_password']).first()
            if u is None:
                return jsonify(message="User not found.")
            db.session.delete(u)
            db.session.commit()
            return jsonify(message="The user has been successfully deleted.")
        except Exception as e:
            print(str(e))
            return jsonify(message="The user could not be deleted. This could be due to the parameters you sent. If the problem still persists, contact us.")

class HEventResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_name", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("user_email", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("user_password", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("e_text", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("e_date", type=datetime.datetime, required=True, location=("json", "values"))
        self.parser.add_argument("new_e_text", type=str, required=True, location=("json", "values"))
        self.parser.add_argument("new_e_date", type=datetime.datetime, required=True, location=("json", "values"))
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