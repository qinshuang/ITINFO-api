#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: DatasMixin.py
@time: 2019/01/02
"""

from app import db
from app.commons.errors import RequestParmsError, DuplicateDataError
from sqlalchemy.exc import IntegrityError


class DatasMixin(object):

    def __init__(self, SCHEMA, T):
        self.SCHEMA = SCHEMA
        self.T = T

    def get_all(self):
        datas = db.session.query(self.T).all()
        return self.SCHEMA().dump(datas, many=True)

    def create_one(self, data):
        if not data:
            raise RequestParmsError
        try:
            new_t = self.T(**data)
            db.session.add(new_t)
            db.session.commit()
        except IntegrityError:
            raise DuplicateDataError
        except BaseException as e:
            raise RequestParmsError
        return {"msg": "Create Success"}

    def get_one(self, id):
        data = db.session.query(self.T).filter_by(id=id).one()
        return self.SCHEMA().dump(data)

    def delete(self, id):
        data = id
        if not data:
            raise RequestParmsError
        try:
            t = db.session.query(self.T).filter_by(id=id).one()
            db.session.delete(t)
            db.session.commit()
        except BaseException as e:
            raise RequestParmsError
        return {"msg": "Delete Success"}


