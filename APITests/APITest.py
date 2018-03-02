import TestFramework.Test

from suds.client import Client

class APITest(TestFramework.Test.BaseTest):
    'Base class for ReSTful Web API tests'
    def __init__(self, baseURL):
        from simple_rest_client.api import API
        self.baseURL = baseURL
        self.api = API(
            api_root_url = baseURL, # base api url
            params={}, # default params
            headers={}, # default headers
            timeout=2, # default timeout in seconds
            append_slash=False, # append slash to final url
            json_encode_body=True, # encode body as json
        )
        self.cookie = None

    def login(self, username, password):
        self.api.add_resource(resource_name="users")
        req_body = {"Username":  username, "Password": password}
        response = self.sendPostRequest(self.api.users, req_body)
        self.cookie = response.headers["Set-cookie"]

    def sendGetRequest(self, resource):
        headers = {"Cookie": self.cookie }
        response = resource.list(body=None, headers=headers)
        if (response.status_code != 200):
            raise RuntimeError("Error executing query over " + resource.name)
        return response

    def sendPostRequest(self, resource, req_body):
        response = resource.create(body=req_body, headers={"content-length": str(len(req_body)), "content-type": "application/json", "cookie": self.cookie})
        if (response.status_code != 200):
            raise RuntimeError("Error executing query over " + resource.name)
        return response