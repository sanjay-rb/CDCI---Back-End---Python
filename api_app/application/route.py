from application import app, api
from flask_restplus import Resource, reqparse, fields
from flask import request, render_template, jsonify

clac = [
    {
        'name': "/sum",
        'input': 2,
        'output': 1,
        'req': ['GET', 'POST'],
    },
    {
        'name': "/sub",
        'input': 2,
        'output': 1,
        'req': ['GET', 'POST'],
    },
    {
        'name': "/mul",
        'input': 2,
        'output': 1,
        'req': ['GET', 'POST'],
    },
    {
        'name': "/div",
        'input': 2,
        'output': 1,
        'req': ['GET', 'POST'],
    },
]
    
################################################ API #################################################################
@api.route('/clac')
class Calc(Resource):
    def get(self):
        return clac

dataParser = reqparse.RequestParser()
dataParser.add_argument(default=0, type=int, name='num1')
dataParser.add_argument(default=0, type=int, name='num2')

bodyParser = api.model(
    name='Numbers', model={
        'num1': fields.Integer,
        'num2': fields.Integer,
    }
)

@api.route('/sum')
class Sum(Resource):
    @api.expect(dataParser)
    def get(self):
        args = dataParser.parse_args(request)
        num1 = args.get('num1')
        num2 = args.get('num2')
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 + num2,
        }
    @api.expect(bodyParser)
    def post(self):
        print(api.payload)
        num1 = api.payload['num1']
        num2 = api.payload['num2']
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 + num2,
        }

@api.route('/sub')
class Sub(Resource):
    @api.expect(dataParser)
    def get(self):
        args = dataParser.parse_args(request)
        num1 = args.get('num1')
        num2 = args.get('num2')
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 - num2,
        }
    @api.expect(bodyParser)
    def post(self):
        num1 = api.payload['num1']
        num2 = api.payload['num2']
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 - num2,
        }

@api.route('/mul')
class Mul(Resource):
    @api.expect(dataParser)
    def get(self):
        args = dataParser.parse_args(request)
        num1 = args.get('num1')
        num2 = args.get('num2')
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 * num2,
        }
    @api.expect(bodyParser)
    def post(self):
        num1 = api.payload['num1']
        num2 = api.payload['num2']
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 * num2,
        }

@api.route('/div')
class Div(Resource):
    @api.expect(dataParser)
    def get(self):
        args = dataParser.parse_args(request)
        num1 = args.get('num1')
        num2 = args.get('num2')
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 / num2,
        }
    @api.expect(bodyParser)
    def post(self):
        num1 = api.payload['num1']
        num2 = api.payload['num2']
        return {
            'Number 1': num1,
            'Number 2': num2,
            'Result': num1 / num2,
        }
################################################ END #################################################################

################################################ ROUTE ###############################################################

@app.route('/index')
@app.route('/index/')
@app.route('/home')
@app.route('/home/')
def index():
    return render_template('index.html')

################################################ END #################################################################
