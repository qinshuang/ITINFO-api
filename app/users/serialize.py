#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: serialize.py
@time: 2019/01/02
"""
from flask_marshmallow import Schema
from .models import *


class RoleSchema(Schema):
    class Meta:
        model = Role
        fields = ('id', 'name')
