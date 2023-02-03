import jsonschema
import requests
import pytest


class TestUsersRequest:
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "email": {"type": "string"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "avatar": {"type": "string"},
        },
        "required": ["id"],
        "additionalProperties": False
    }

    def test_user_request_positive(self, getUser):
        user = getUser

        response = requests.get('https://reqres.in/api/users/' + str(user['id']))

        assert response.status_code == 200
        jsonschema.validate(response.json()['data'], schema=self.schema)

    def test_user_request_negative(self, getInvalidId):
        response = requests.get('https://reqres.in/api/users/' + str(getInvalidId))

        assert response.status_code == 404



