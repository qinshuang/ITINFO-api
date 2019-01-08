#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: serialize.py
@time: 2019/01/02
"""
from flask_marshmallow import Schema
from marshmallow import fields
from .models import *
from . import ma
class RoleSchema(Schema):
    class Meta:
        model = Role
        fields = ('id', 'name')


class UserSchema(Schema):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'active', 'first_name', 'last_name','roles')

    roles = fields.Nested(RoleSchema, many=True)