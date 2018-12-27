#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: errors.py
@time: 2018/10/15
"""

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
    }