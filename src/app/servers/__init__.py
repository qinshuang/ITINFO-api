#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py
@time: 2019/01/08
"""


from flask import Blueprint
from flask_restful import Api
from app.commons.errors import errors
from flask_marshmallow import Marshmallow

servers = Blueprint('servers', __name__)
api = Api(servers, errors=errors)
ma = Marshmallow(api)

from . import views