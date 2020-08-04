import requests
import json
import itertools as it
from . import exceptions
from .config import *

class WebSession:
    def __init__(self, cookies):
        self.session = requests.Session()
        self.session.cookies = requests.cookies.cookiejar_from_dict(cookies)


class WebAgent(WebSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def graphql_request(self, payload):
        ss = self.session
        response = ss.get(GRAPHQL_URL, params = payload)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Client exited with status code {response.status_code}, PAYLOAD :{payload}, COOKIES:{ss.cookies}, {response.text}, check your settings"
            )
        obj = response.json()
        st = obj.get('status', None)
        if st and st == 'fail':
            raise exceptions.GraphQLException(obj)
        return obj
