import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('Config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
                    "first_name": "Kledson",
                    "last_name": "Vinicius",
                    "cpf": "320.380.970-20",
                    "email": "kledson16@gmail.com",
                    "birth_date": "2002-07-02"
                }

    @pytest.fixture
    def invalid_user(self):
        return {
                    "first_name": "Kledson",
                    "last_name": "Vinicius",
                    "cpf": "320.380.970-21",    # CPF Invalid
                    "email": "kledson16@gmail.com",
                    "birth_date": "2002-07-02"
                }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 201
        assert b"User created success." in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"CPF is invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user['cpf'])
        assert response.status_code == 200
        assert response.json[0]['cpf'] == "320.380.970-20"

        response = client.get('/user/%s' % invalid_user['cpf'])
        assert response.status_code == 400
        assert b"user does not exist." in response.data
