#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2019/01/02
"""
from . import api
from .serialize import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token

from app.commons.DatasMixin import DatasMixin
from app.commons.decorators import roles_required
from flask_jwt_extended import get_current_user
parser = reqparse.RequestParser()
parser.add_argument('rolename', type=str, help='rolename')


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, help='username')

class UserLogin(Resource):

    def post(self):
        args = login_parser.parse_args()

        #     user = User.find_by_openid(args['openid'])
        #     if not user:
        #         User(username=args['openid'], email='', openid=args['openid']).save_to_db()
        access_token = create_access_token(identity=args['username'])
        user = get_current_user()
        return {
            'message': 'User {} was created'.format(args['username']),
            'access_token': access_token
        }

role_parser = reqparse.RequestParser()
role_parser.add_argument('rolename', type=str, help='rolename')


class RolesManage(Resource):
    obj = DatasMixin(RoleSchema, Role)

    def get(self):
        return self.obj.get_all()

    def post(self):
        args = role_parser.parse_args()
        rolename = args.get("rolename")
        return self.obj.create_one({"name": rolename})


class OneRoleManage(Resource):
    obj = DatasMixin(RoleSchema, Role)

    def get(self, id):
        return self.obj.get_one(id)

    def delete(self, id):
        return self.obj.delete(id)


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, help='username', required=True)
user_parser.add_argument('email', type=str, help='email', required=True)
user_parser.add_argument('first_name', type=str, help='first_name', required=True)
user_parser.add_argument('last_name', type=str, help='last_name', required=True)


class UserManage(Resource):
    obj = DatasMixin(UserSchema, User)

    def get(self):
        ret = UserSchema().dump(User.get_all(), many=True)
        return ret.data

    @jwt_required
    @roles_required("SuperAdmin")
    def post(self):
        args = user_parser.parse_args()
        username = args.get("username")
        email = args.get("email")
        first_name = args.get("first_name")
        last_name = args.get("last_name")
        return self.obj.create_one({"username": username,
                                    "email": email,
                                    "first_name": first_name,
                                    "last_name": last_name,
                                    "active":True,
                                    "password": "123456"})


user_role_parser = reqparse.RequestParser()
user_role_parser.add_argument('username', type=str, help='username', required=True)
user_role_parser.add_argument('rolename', type=str, help='rolename', required=True)


class UserRoleManage(Resource):

    def post(self):
        args = user_role_parser.parse_args()
        username = args.get("username")
        rolename = args.get("rolename")
        User.update_roles(username, rolename)
        return {"msg": "Update Success"}


api.add_resource(UserLogin, '/login')
api.add_resource(RolesManage, '/role/manage/')
api.add_resource(OneRoleManage, '/role/manage/<int:id>')
api.add_resource(UserManage, '/user/manage/')
api.add_resource(UserRoleManage, '/userroles/manage/')
