#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py.py
@time: 2019/01/02
"""

from flask import Blueprint
from flask_restful import Api
from app.errors import errors

users = Blueprint('users', __name__)
api = Api(users, errors=errors)

from . import views