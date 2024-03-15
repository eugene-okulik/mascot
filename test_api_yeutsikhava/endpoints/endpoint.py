import allure
import requests


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that price is the same as sent')
    def check_response_title_is_correct(self, expected_price):
        actual_price = self.json['data']['price']
        assert actual_price == expected_price, f"Expected price {expected_price}, but got {actual_price}"

    @allure.step('Check that the object name is correct')
    def check_name_of_an_object(self, expected_name):
        actual_name = self.json['name']
        assert actual_name == expected_name, f"Expected name '{expected_name}', but got '{actual_name}'"

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Verify object not found or bad request after deletion')
    def verify_not_found_or_bad_request(self, object_id):
        response = requests.get(f"{self.url}/{object_id}")
        assert response.status_code in [400, 404], f"Unexpected status code: {response.status_code}"
