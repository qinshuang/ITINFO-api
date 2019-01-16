#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: models.py
@time: 2019/01/08
"""
from app import db
from datetime import datetime


class Server(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.Integer())  # 1 new 2 setup 3 running 4 decommission 5 non-operation
    server_name = db.Column(db.String(255), nullable=False, unique=True)
    device_type = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(15))
    ip_zone = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    cpu = db.Column(db.String(50), nullable=False)
    memory = db.Column(db.String(50), nullable=False)
    disk_type = db.Column(db.String(50), nullable=False)
    disk_volume = db.Column(db.String(50), nullable=False)
    prod_server = db.Column(db.Boolean, default=False)
    backup = db.Column(db.Boolean, default=False)
    comments = db.Column(db.String(255))
    normal_users = db.Column(db.String(255))
    sudo_users = db.Column(db.String(255))
    application_install = db.Column(db.String(255))
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    update_time = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def update_server_by_id(cls, id, **kwargs):
        server = db.session.query(cls).filter_by(id=id).first()
        if kwargs:
            for k, v in kwargs.items():
                if v is not None:
                    setattr(server, k, v)
            db.session.commit()
