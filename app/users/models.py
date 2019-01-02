#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: models.py
@time: 2019/01/02
"""
from app import db
from flask_login import UserMixin


# Define the User data-model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # Relationships
    roles = db.relationship('Role', secondary='user_roles')


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    @classmethod
    def list(cls):
        return db.session.query(cls).all()

    @classmethod
    def create(cls, rolername):
        new_role = Role()
        new_role.status = rolername
        db.session.add(new_role)
        db.session.commit()
        return new_role

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
