from flask import jsonify
from flask_restful import Resource, reqparse
from .model import UserModel, HealthCheckModel
import re
import traceback


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")


class HealthCheck(Resource):
    def get(self):
        response = HealthCheckModel.objects(status="healthcheck")
        if response:
            return "Healthy", 200
        HealthCheckModel(status="healthcheck").save()
        return "Healthy", 200


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def validate_cpf(self, cpf):
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False
        sum_of_products = sum(a * b for a, b in zip(numbers[0:9],
                                                    range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False
        sum_of_products = sum(a * b for a, b in zip(numbers[0:10],
                                                    range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()
        if not self.validate_cpf(cpf=data['cpf']):
            return {"statusCode": 400, "message": "CPF is invalid"}, 400
        if UserModel.objects(cpf=data['cpf']).first():
            return {"statusCode": 400,
                    "message":
                        "CPF already exists in database."}, 400
        if UserModel.objects(email=data['email']).first():
            return {"statusCode": 400,
                    "message":
                        "Email already exists in database."}, 400
        try:
            result = UserModel(**data)
            result.save()
            return {"statusCode": 201,
                    "message":
                        "User created success."}, 201
        # except NotUniqueError:
        #     return {"statusCode": 400,
        #             "message":
        #                 "CPF already exists in database."}, 400
        except Exception:
            print(f"Unexpected error: {traceback.format_exc()}")
            return {"statusCode": 500,
                    "message":
                        "An unexpected error occurred."}, 500

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)
        if response:
            return jsonify(response)

        return {"statusCode": 400, "message": "user does not exist."}, 400

    def patch(self):
        data = _user_parser.parse_args()
        if not self.validate_cpf(cpf=data['cpf']):
            return {"statusCode": 400, "message": "CPF is invalid"}, 400
        if not UserModel.objects(cpf=data['cpf']).first():
            return {"statusCode": 400,
                    "message":
                        "CPF not exists in database."}, 400
        if UserModel.objects(email=data['email']).first():
            return {"statusCode": 400,
                    "message":
                        "Email already exists in database."}, 400

        response = UserModel.objects(cpf=data['cpf'])
        try:
            response.update(**data)
            return {"statusCode": 200,
                    "message":
                        "User updated success."}, 200
        # except NotUniqueError:
        #     return {"statusCode": 400,
        #             "message":
        #                 "CPF already exists in database."}, 400
        except Exception:
            print(f"Unexpected error: {traceback.format_exc()}")
            return {"statusCode": 500,
                    "message":
                        "An unexpected error occurred."}, 500

    def delete(self, cpf):
        response = UserModel.objects(cpf=cpf)
        if response:
            response.delete()
            return {"status_code": 200, "message": "User deleted."}, 200

        return {"status_code": 400, "message": "User does not exist."}, 400
