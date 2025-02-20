from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)


db = MongoEngine()
app.config['MONGODB_SETTINGS'] = [
    {
        "db": "users",
        "host": "mongodb",
        "port": 27017,
        "alias": "default",
        "user":"admin",
        "password":"admin"
    }
]

class Users(Resource):
    def get(self):
        return {"statusCode": 200, "message": "list users"}


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
