import requests
from requests.adapters import HTTPAdapter
from urllib3.contrib.appengine import is_appengine_sandbox
from requests_toolbelt.adapters import appengine
from modules.auth import Auth 
from modules.database import Database
from utils.endpoint_master import EndpointMaster


class Firebase():
    def __init__(self, config) -> None:
        self.api_key = config["apiKey"]
        self.auth_domain = config["authDomain"]
        self.database_url = config["databaseURL"]
        self.storage_bucket = config["storageBucket"]
        self.credentials = None
        self.requests = requests.Session()
        if is_appengine_sandbox():
            # AppEngineManager uses AppEngine's URLFetch API behind the scenes
            http = appengine.AppEngineAdapter()
        else:
            # PoolManager uses a socket-level API behind the scenes
            http = HTTPAdapter()

        for scheme in ('http://', 'https://'):
            self.requests.mount(scheme, http)

    def auth(self):
        return Auth(EndpointMaster(self.api_key, "auth"), self.requests, self.credentials)

    def database(self):
        return Database(EndpointMaster(self.api_key, "database"), self.requests, self.credentials)

