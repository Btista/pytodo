from flask import Flask
from flask import render_template
from flask import jsonify, make_response, request
import sys
sys.path.append("..")
from flaskr import app
from flaskext.mysql import MySQL
print('aa')
mysql = MySQL()
mysql.init_app(app)

@app.route('/add', methods=['POST'])
def add():
    if(request.method == 'POST'):
        conn = mysql.connect()
        cursor = conn.cursor()
        data = request.json
        sql_command = """insert into `xisitan`.`todolist` (`create_time`, `status`, `title`, `user_id`) values ({}, {}, '{}', {})
        """.format(data['create_time'],data['status'],data['title'],123)
        cursor.execute(sql_command)
        response ={            
            'code': 200,
            'message': "success hardcode",
            'data': request.json
        }
        conn.commit()
        conn.close()
        response_body = make_response(jsonify(response),200)
        print(request.form)
        return response_body