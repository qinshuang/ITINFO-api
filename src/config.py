#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: config.py
@time: 2018/10/15
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    HOST = "0.0.0.0"
    PORT = 5000
    JWT_SECRET_KEY = "1234"
    SQLALCHEMY_ECHO=True
    @staticmethod
    # 此注释可表明使用类名可以直接调用该方法
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "DEVELOPMENT"

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:123456@127.0.0.1/itinfo'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
