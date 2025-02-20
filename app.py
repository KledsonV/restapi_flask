from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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

if __name__ == "__main__":
    app.run(debug=True)
