import requests


def object_creation():
    body = {
        "name": "Xiaomi Redmibook Pro 13.3",
        "data": {
            "year": 2023,
            "price": 3203.67,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers)
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['price'] == 3203.67, 'Price is incorrect'


object_creation()


def object_new():
    body = {
        "name": "Xiaomi Mi Book Pro",
        "data": {
            "year": 2023,
            "price": 3201.67,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB",
            "Colour": "Black"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers)
    return response.json()['id']


object_new()


def clear(object_id):
    requests.delete('https://api.restful-api.dev/objects/{object_id}')


def object_update():
    object_id = object_new()
    body = {
        "name": "Xiaomi Redmibook Pro 14",
        "data": {
            "year": 2023,
            "price": 3201.67,
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
    assert response['name'] == "Xiaomi Redmibook Pro 14"
    clear(object_id)


object_update()


def object_patch():
    object_id = object_new()
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
    print(response)
    clear(object_id)


object_patch()


def object_deletion():
    object_id = object_new()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print(response.json())
    print(response.status_code)


object_deletion()
