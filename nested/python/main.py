import functions_framework
import json
from flask import Request

@functions_framework.http
def hello_world(request : Request):
    """OpenFunction HTTP handler function"""
    try:
        if request.method == 'GET':
            name = request.args.get('name', 'World')
        elif request.method == 'POST':
            request_json = request.get_json(silent=True)
            name = request_json.get('name', 'World') if request_json else 'World'
        else:
            return f"Method {request.method} not allowed", 405
            
        response = {
            "message": f"Hello, {name}!",
            "status": "success",
            "function": "openfunction-python-sample"
        }
        
        return json.dumps(response), 200, {'Content-Type': 'application/json'}
        
    except Exception as e:
        error_response = {"error": str(e), "status": "error"}
        return json.dumps(error_response), 500, {'Content-Type': 'application/json'}
