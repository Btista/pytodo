from flask import Flask
from flask import request
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.config['MYSQL_DATABASE_HOST']='localhost'
    app.config['MYSQL_DATABASE_USER']='root'
    app.config['MYSQL_DATABASE_PASSWORD']='password'
    app.config['MYSQL_DATABASE_DB']='xisitan'
    return app

app = create_app()

