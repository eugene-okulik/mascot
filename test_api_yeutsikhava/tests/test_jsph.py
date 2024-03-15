import pytest

payload = {
    "name": "Apple Macbook Air M3",
    "data": {"year": 2024, "price": 1500.99, "CPU model": "Intel Core i7", "Hard disk size": "512 GB", "Colour": "Gold"}
}

TEST_DATA = [
    ({"name": "Xiaomi Redmi book Pro 13.3",
      "data": {"year": 2023, "price": 3203.67, "CPU model": "Intel Core i7", "Hard disk size": "512 GB"}}),
    ({"name": "Xiaomi Mi Book Pro",
      "data": {"year": 2023, "price": 3201.67, "CPU model": "Intel Core i5", "Hard disk size": "256 GB",
               "Colour": "Silver"}}),
    ({"name": "Asus ZenBook 14",
      "data": {"year": 2023, "price": 1500.99, "CPU model": "Intel Core i5", "Hard disk size": "1 TB",
               "Colour": "Blue"}})
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_object_creation(create_object_endpoint, data, calculate_expected_price):
    create_object_endpoint.new_object(payload=data)
    create_object_endpoint.check_status_is_200()
    expected_price = calculate_expected_price(data['data']['price'])
    create_object_endpoint.check_response_title_is_correct(expected_price)


def test_object_update(update_object_endpoint, object_id):
    update_object_endpoint.object_update(object_id, payload)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_name_of_an_object(payload['name'])


def test_object_patch(patch_object_endpoint, object_id):
    patch_object_endpoint.object_patch(object_id, payload)
    patch_object_endpoint.check_name_of_an_object(payload['name'])


def test_object_deletion(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_by_id(object_id)
    delete_object_endpoint.verify_not_found_or_bad_request(object_id)
