#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: errors.py
@time: 2018/10/15
"""
from flask_restful import HTTPException


class RequestParmsError(HTTPException):
    pass


errors = {
        'UserAlreadyExistsError': {
            'message': "A user with that username already exists.",
            'status': 409,
        },
        'ResourceDoesNotExist': {
            'message': "A resource with that ID no longer exists.",
            'status': 410,
            'extra': "Any extra information you want.",
        },
        'RequestParmsError': {
            'message': "Request Parms Error",
            'status': 400,
            'extra': "Any extra information you want.",
        },
    }

