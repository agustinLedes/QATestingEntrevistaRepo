import pytest
import requests


@pytest.fixture
def getUser():
    response = requests.get('https://reqres.in/api/users')

    return response.json()['data'][0]

@pytest.fixture
def getInvalidId():
    pageParams = {'page': 1, 'per_page': 10}
    response = requests.get('https://reqres.in/api/users', params=pageParams)

    return response.json()['total'] + 10



