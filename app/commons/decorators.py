#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: decorators.py
@time: 2019/01/07
"""
from flask_jwt_extended import get_jwt_claims
from functools import wraps
from errors import NoPermissionError


def roles_required(*role_names):
    def wrapper(view_function):
        @wraps(view_function)  # Tells debuggers that is is a function wrapper
        def decorator(*args, **kwargs):
            if role_names is None:
                return view_function(*args, **kwargs)
            user = get_jwt_claims()
            for role in user.get('roles'):
                if role.get('name') in role_names:
                    # It's OK to call the view
                    return view_function(*args, **kwargs)

            raise NoPermissionError

        return decorator

    return wrapper
