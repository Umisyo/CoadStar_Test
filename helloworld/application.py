#!flask/bin/python
# coading: utf-8

import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/test', methods=['GET'])
def test_get():
    hoge:str = 'hoge'
    return hoge 


if __name__ == '__main__':
    flaskrun(application)
