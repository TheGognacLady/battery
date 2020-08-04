from aiohttp import ClientResponseError
from requests.exceptions import HTTPError



class InstagramException(Exception):
    pass

class GraphQLException(InstagramException):
    def __init__(self, obj):
        super().__init__(f"Bad request for GRAPHQL API {obj}")
        
