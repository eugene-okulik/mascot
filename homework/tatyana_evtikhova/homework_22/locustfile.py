from locust import HttpUser, task, between


class ApiUser(HttpUser):
    wait_time = between(0.5, 2)

    @task(1)
    def create_update_patch_and_delete_object(self):
        create_payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2899.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        create_response = self.client.post("/objects", json=create_payload)
        object_id = create_response.json().get('id', None) if create_response.ok else None

        if object_id:
            update_payload = {
                "name": "Apple MacBook Pro 14",
                "data": {
                    "year": 2019,
                    "price": 2300.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }
            self.client.put(f"/objects/{object_id}", json=update_payload)

            patch_payload = {
                "name": "Apple MacBook Pro 14",
                "data": {
                    "year": 2019,
                    "price": 2199.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }
            self.client.patch(f"/objects/{object_id}", json=patch_payload)

            self.client.delete(f"/objects/{object_id}")

    @task(3)
    def create_object(self):
        create_payload = {
                "name": "Apple MacBook Air",
                "data": {
                    "year": 2017,
                    "price": 870.23,
                    "CPU model": "Intel Core i5",
                    "Hard disk size": "128 Gb"
                }
            }
        create_response = self.client.post("/objects", json=create_payload)
        