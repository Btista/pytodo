from flask import Flask, render_template, jsonify, make_response, request
import sys
sys.path.append("..")
from flaskr import app
from flaskr.models.base import database, todoModel
from flaskr.api.common import RESTful
from flask_restful import Resource,Api
# from flaskext.mysql import MySQL
# mysql = MySQL()
# mysql.init_app(app)

api=Api(app)

class getList(Resource):
    def get(self):
        list = todoModel.select().limit(1000).dicts()
        list = [item for item in list]
        return RESTful.response(code=200, data=list)

class add(Resource):
    def post(self):
        data = request.json
        list = todoModel.create(name=data['name'], event=data['event'], begin_time= data['begin_time'], if_done=data['if_done'])
        list.save()    
        return RESTful.response(code=200, data=data)

class delete(Resource):
    def post(self):
        data = request.json
        id = data['id']
        item_for_delete = todoModel.get(todoModel.id==id)
        item_for_delete.delete_instance()
        return RESTful.response(code=200, data=data)

class update(Resource):
    def post(self):
        data = request.json
        query = todoModel.update(name=data['name'], event=data['event'], begin_time= data['begin_time'], if_done=data['if_done']).where(todoModel.id == data['id'])
        query.execute()
        return RESTful.response(code=200, data=data)

api.add_resource(getList,'/list')
api.add_resource(add,'/add')
api.add_resource(delete,'/delete')
api.add_resource(update,'/update')
