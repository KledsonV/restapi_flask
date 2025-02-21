from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = [
    {
        "db": "users",
        "host": "mongodb_restapi",
        "port": 27017,
        "username": "admin",
        "password": "admin"
    }
]
db = MongoEngine()


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    fist_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    birth_date = db.DateTimeField(required=True, unique=True)


class Users(Resource):
    def get(self):
        return {"statusCode": 200, "message": jsonify(UserModel.objects())}


class User(Resource):
    def post(self):
        return {"statusCode": 200, "message": "user[0]"}

    def get(self, cpf):
        return {"statusCode": 200, "message": "CPF: " + cpf}


api.add_resource(Users, "/users")
api.add_resource(User, "/user", "/user/<string:cpf>")

db.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
