#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2019/01/02
"""
from . import api
from app.errors import RequestParmsError
from .models import *
from .serialize import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token

from flask_user import roles_required
from app.commons.DatasMixin import DatasMixin

parser = reqparse.RequestParser()
parser.add_argument('pk', type=int, help='PK cannot be converted')
parser.add_argument('username', type=str, help='username')
parser.add_argument('rolename', type=str, help='rolename')
parser.add_argument('datas', help='datas')

class UserRegistration(Resource):
    def post(self):
        args = parser.parse_args()
        #     user = User.find_by_openid(args['openid'])
        #     if not user:
        #         User(username=args['openid'], email='', openid=args['openid']).save_to_db()
        access_token = create_access_token(identity=args['username'])

        return {
            'message': 'User {} was created'.format(args['username']),
            'access_token': access_token
        }


class RolesManage(Resource):
    obj = DatasMixin(RoleSchema, Role)

    def get(self):
        return self.obj.get_all()

    def post(self):
        args = parser.parse_args()
        return self.obj.create_many(args.get("datas"))


class OneRoleManage(Resource):
    obj = DatasMixin(RoleSchema, Role)

    def get(self, id):
        return self.obj.get_one(id)

    def delete(self, id):
        return self.obj.delete(id)


api.add_resource(UserRegistration, '/user/registration')
api.add_resource(RolesManage, '/role/manage/')
api.add_resource(OneRoleManage, '/role/manage/<int:id>')
