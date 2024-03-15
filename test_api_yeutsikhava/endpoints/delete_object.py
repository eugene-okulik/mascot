import requests
import allure

from test_api_yeutsikhava.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    def __init__(self):
        super().__init__()
        self.response = None

    @allure.step('Delete an object')
    def delete_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
