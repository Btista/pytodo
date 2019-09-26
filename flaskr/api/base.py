from flask import Flask, render_template, jsonify, make_response, request
import sys
sys.path.append("..")
from flaskr import app
from flaskr.models.base import database, todoModel
import json
import requests
# from flaskext.mysql import MySQL
# mysql = MySQL()
# mysql.init_app(app)

@app.route('/list', methods=['GET'])
def getList():
    if(request.method == "GET"):
        list = todoModel.select().limit(1000).dicts()
        list = [item for item in list]
        response ={            
            'code': 200,
            'message': "success hardcode",
            'data':list
        }
        response_body = make_response(jsonify(response),200)
        return response_body

@app.route('/add', methods=['POST'])
def add():
    if(request.method == 'POST'):
        data = request.json
        print(request.json)
        list = todoModel.create(name=data['name'], event=data['event'], begin_time= data['begin_time'], if_done=data['if_done'])
        list.save()    
        response ={            
            'code': 200,
            'message': "success hardcode",
            'data': request.json
        }
        response_body = make_response(jsonify(response),200)
        return response_body

@app.route('/delete', methods=['POST'])
def delete():
    if(request.method == 'POST'):
        data = request.json
        id = data['id']
        item_for_delete = todoModel.get(todoModel.id==id)
        item_for_delete.delete_instance()
        response ={            
            'code': 200,
            'message': "success hardcode",
            'data': request.json
        }
        response_body = make_response(jsonify(response),200)
        return response_body

@app.route('/update', methods=['POST'])
def update():
    if(request.method == 'POST'):
        data = request.json
        query = todoModel.update(name=data['name'], event=data['event'], begin_time= data['begin_time'], if_done=data['if_done']).where(todoModel.id == data['id'])
        query.execute()
        response ={            
            'code': 200,
            'message': "success hardcode",
            'data': request.json
        }
        response_body = make_response(jsonify(response),200)
        return response_body
