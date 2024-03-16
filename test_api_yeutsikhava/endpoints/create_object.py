import requests
import allure

from test_api_yeutsikhava.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    def __init__(self):
        super().__init__()
        self.response = None
        self.json = None

    @allure.step('Create new Object')
    def new_object(self, payload):
        self.response = requests.post(
            self.url,
            json=payload,
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
