#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2018/12/27
"""

from . import api
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token


class DemoView(Resource):
    @jwt_required
    def get(self):
        return {1: 1}


api.add_resource(DemoView, '/demo')
