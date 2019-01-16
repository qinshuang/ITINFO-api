#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: models.py
@time: 2019/01/08
"""
from app import db
from sqlalchemy.sql import func


class Server(db.Model):
    __tablename__ = 'servers'

    status = db.Integer()  # 1 new 2 setup 3 running 4 decommission 5 non-operation
    server_name = db.Column(db.String(255), nullable=False, unique=True)
    device_type = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    cpu = db.Column(db.String(50), nullable=False)
    memory = db.Column(db.String(50), nullable=False)
    disk_type = db.Column(db.String(50), nullable=False)
    disk_volume = db.Column(db.String(50), nullable=False)
    prod_server = db.Boolean()
    backup = db.Boolean()
    comments = db.Column(db.String(255))
    normal_users = db.Column(db.String(255))
    sudo_users = db.Column(db.String(255))
    application_install = db.Column(db.String(255))
    start_time = db.DATETIME(default=func.now())
    update_time = db.DATETIME(default=func.now(), onupdate=func.now())

