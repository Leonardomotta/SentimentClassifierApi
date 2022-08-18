
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from Modelo.twitterClassifier import predict
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)


cors = CORS(app, resources={r"/users": {"origins": "*"}})
cors = CORS(app, resources={r"/cad": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'


class Users(Resource):
    def get(self):
        candidato = request.args.get('candidato')
        ano = request.args.get('ano')
        return jsonify(predict(candidato,ano))
              

class UserById(Resource):
    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("delete from user where id=%d " % int(id))
        return {"status": "success"}

    def get(self, id):
    
        result = ""
        return jsonify(result)

api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
