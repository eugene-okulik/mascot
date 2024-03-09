import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def print_session_messages():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def run_around_tests():
    print("before test")
    yield
    print("after test")


@pytest.fixture
def object_fixture():
    object_id = object_new()
    yield object_id
    clear(object_id)


def clear(object_id):
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.mark.parametrize("body", [
    ({
        "name": "Xiaomi Redmibook Pro 13.3",
        "data": {
            "year": 2023,
            "price": 3203.67,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    }),
    ({
        "name": "Xiaomi Mi Book Pro",
        "data": {
            "year": 2023,
            "price": 3201.67,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB",
            "Colour": "Silver"
        }
    }),
    ({
        "name": "Asus ZenBook 14",
        "data": {
            "year": 2023,
            "price": 1500.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "1 TB",
            "Colour": "Blue"
        }
    })
])
def test_object_creation(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers)
    assert response.status_code == 200
    assert response.json()['data']['price'] == body['data']['price']


@pytest.mark.critical
def test_object_update(object_fixture):
    object_id = object_fixture
    body = {
        "name": "Xiaomi Redmibook Pro 14",
        "data": {
            "year": 2023,
            "price": 3188.03,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB",
            "Colour": "Black"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == body['name']


@pytest.mark.medium
def test_object_patch(object_fixture):
    object_id = object_fixture
    body = {
        "name": "Xiaomi Redmibook 14(Updated Name)",
        "data": {
            "year": 2023,
            "price": 3201.67,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB",
            "Colour": "Black"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers).json()
    assert response['name'] == body['name']


def test_object_deletion(object_fixture):
    object_id = object_fixture
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.status_code == 200


def object_new():
    body = {
        "name": "Testing Object",
        "data": {
            "year": 2023,
            "price": 999.99,
            "CPU model": "Intel Core i3",
            "Hard disk size": "128 GB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers)
    return response.json()['id']
