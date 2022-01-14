import flask
import traceback
import subprocess

from flask import jsonify
from http import HTTPStatus
import json

script_apis=flask.Blueprint('scripts', __name__)

@script_apis.route('/run/<id>',methods=['POST'])
def run_script(id):
    try:
        req=flask.request.json
        result=subprocess.run(['python', f'scripts/{id}.py', json.dumps(req)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output=str(result.stdout)
        err=str(result.stderr)
        return jsonify({'output':output,'error':err}), HTTPStatus.OK
    except Exception as e:
        return jsonify({'error_message': traceback.format_exc()}), HTTPStatus.INTERNAL_SERVER_ERROR