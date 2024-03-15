import requests
import allure

from test_api_yeutsikhava.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    def __init__(self):
        super().__init__()
        self.response = None
        self.json = None

    @allure.step('Update an object')
    def object_update(self, object_id, payload):
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload)
        self.json = self.response.json()
        return self.response
