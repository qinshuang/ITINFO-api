#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2018/12/27
"""

from . import api
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required,create_access_token

parser = reqparse.RequestParser()
parser.add_argument('pk', type=int, help='PK cannot be converted')
parser.add_argument('username', type=str, help='username')

class DemoView(Resource):
    @jwt_required
    def get(self):
        return {1: 1}

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

api.add_resource(DemoView, '/demo')
api.add_resource(UserRegistration, '/user/registration')
