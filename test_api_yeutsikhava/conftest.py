import pytest
from test_api_yeutsikhava.endpoints.create_object import CreateObject
from test_api_yeutsikhava.endpoints.update_object import UpdateObject
from test_api_yeutsikhava.endpoints.patch_object import PatchObject
from test_api_yeutsikhava.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id():
    create_object = CreateObject()
    payload = {
        "name": "Testing Object",
        "data": {
            "year": 2024,
            "price": 999.99,
            "CPU model": "Intel Core i3",
            "Hard disk size": "128 GB"
        }
    }
    create_object.new_object(payload)
    object_id = create_object.json['id']
    yield object_id
    delete_object = DeleteObject()
    delete_object.delete_by_id(object_id)


@pytest.fixture()
def calculate_expected_price():
    def calculation(actual_price):
        return actual_price

    return calculation
