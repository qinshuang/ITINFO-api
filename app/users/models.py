#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: models.py
@time: 2019/01/02
"""
from app import db
from sqlalchemy import or_


# Define the User data-model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Relationships
    roles = db.relationship('Role', secondary='user_roles')

    @classmethod
    def update_roles(cls, username, role_names):
        user = db.session.query(User).filter_by(username=username).first()
        roles = db.session.query(Role).filter(Role.name.in_(role_names.split(","))).all()
        user.roles = roles
        db.session.commit()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_by_username(cls, username):
        return db.session.query(cls).filter(cls.username==username).first()


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
        new_role.name = rolername
        db.session.add(new_role)
        db.session.commit()
        return new_role


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
