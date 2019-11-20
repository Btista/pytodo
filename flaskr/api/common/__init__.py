from flask import make_response, jsonify, request

class RESTful(object):
    def response(code=200, message='', data={}, meta={}, status_code=200):
        if not message:
            if code == 200:
                message = "SUCCESS"
            else:
                message = "FAIL"
        response_data = {
            'code': code,
            'data': data,
            'message': message,
            'meta':meta
        }
        result = make_response(jsonify(response_data),status_code)
        return result