#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: serializes.py
@time: 2019/01/16
"""

from flask_marshmallow import Schema
from .models import *


class ServerSchema(Schema):
    class Meta:
        model = Server
        fields = (
            'id', 'status', 'server_name', 'device_type', 'os', 'ip_zone', 'ip', 'region', 'cpu', 'memory', 'disk_type',
            'disk_volume', 'prod_server', 'backup', 'comments', 'normal_users', 'sudo_users', 'start_time',
            'update_time')
