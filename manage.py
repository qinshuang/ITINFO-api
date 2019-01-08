#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: manage.py
@time: 2018/10/15
"""

import os
from app import create_app, db
from flask_script import Manager
from flask_script.commands import ShowUrls

from flask_migrate import Migrate, MigrateCommand

import logging.config
import yaml

logging.config.dictConfig(yaml.load(open('logging.yml')))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
logger = app.logger
manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('showurls', ShowUrls)
manager.add_command('db', MigrateCommand)

# db models
from app.users.models import *


# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    manager.run()
