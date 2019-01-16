#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2019/01/08
"""

from . import api
from .serializes import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.commons.DatasMixin import DatasMixin
from app.commons.decorators import roles_required
from flask_jwt_extended import get_current_user

server_parser = reqparse.RequestParser()
server_parser.add_argument('status', required=True, type=int,
                           help='1 new 2 setup 3 running 4 decommission 5 non-operation')
server_parser.add_argument('server_name', required=True, type=str, help='')
server_parser.add_argument('device_type', required=True, type=str, help='')
server_parser.add_argument('os', required=True, type=str, help='')
server_parser.add_argument('region', type=str, help='')
server_parser.add_argument('cpu', type=str, help='')
server_parser.add_argument('memory', type=str, help='')
server_parser.add_argument('disk_type', type=str, help='')
server_parser.add_argument('disk_volume', type=str, help='')
server_parser.add_argument('prod_server', type=bool, help='prod_server')
server_parser.add_argument('backup', type=bool, help='backup')
server_parser.add_argument('comments', type=str, help='')
server_parser.add_argument('normal_users', type=str, help='')
server_parser.add_argument('sudo_users', type=str, help='')
server_parser.add_argument('ip_zone', type=str, help='ip_zone', required=True)


class ServersManage(Resource):
    obj = DatasMixin(ServerSchema, Server)

    def get(self):
        return self.obj.get_all()

    @jwt_required
    @roles_required("Admin")
    def post(self):
        args = server_parser.parse_args()
        return self.obj.create_one(dict(
            status=args.get('status'),
            server_name=args.get('server_name'),
            device_type=args.get('device_type'),
            os=args.get('os'),
            region=args.get('region'),
            cpu=args.get('cpu'),
            memory=args.get('memory'),
            disk_type=args.get('disk_type'),
            disk_volume=args.get('disk_volume'),
            prod_server=args.get('prod_server'),
            backup=args.get('backup'),
            comments=args.get('comments'),
            normal_users=args.get('normal_users'),
            sudo_users=args.get('sudo_users'),
            ip_zone=args.get('ip_zone')
        ))


one_server_parser = reqparse.RequestParser()
one_server_parser.add_argument('status', type=int,
                               help='1 new 2 setup 3 running 4 decommission 5 non-operation')
one_server_parser.add_argument('server_name', type=str, help='')
one_server_parser.add_argument('ip', type=str, help='')


class OneServersManage(Resource):
    obj = DatasMixin(ServerSchema, Server)

    def get(self, id):
        return self.obj.get_one(id)

    @jwt_required
    @roles_required("Admin")
    def put(self, id):
        args = one_server_parser.parse_args()
        status = args.get("status", None)
        server_name = args.get("server_name", None)
        ip = args.get("ip", None)
        Server.update_server_by_id(id, status=status, server_name=server_name, ip=ip)
        return self.obj.get_one(id)

    @jwt_required
    @roles_required("Admin")
    def delete(self, id):
        return self.obj.delete(id)


api.add_resource(ServersManage, '/server/manage')
api.add_resource(OneServersManage, '/server/manage/<int:id>')
