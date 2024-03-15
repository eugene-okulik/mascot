import allure
import requests

from test_api_yeutsikhava.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    def __init__(self):
        super().__init__()
        self.response = None
        self.json = None

    @allure.step('Patch an object')
    def object_patch(self, object_id, payload):
        self.response = requests.patch(f"{self.url}/{object_id}", json=payload)
        self.json = self.response.json()
        return self.response