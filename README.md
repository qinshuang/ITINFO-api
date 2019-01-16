[TOC]

# Project: ITINFO-api

# Setup Develop Environments

* python packages required

```python
pip install -r requirements.txt
```
* start project
```bash
cd src
python manage.py runserver -host=0.0.0.0
```

* init database
```sh
create database itinfo at local db

python manage.py db migrade
python manage.py db upgrade

```

* create user
view postman file