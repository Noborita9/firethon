import requests
from requests.adapters import HTTPAdapter
from urllib3.contrib.appengine import is_appengine_sandbox
from requests_toolbelt.adapters import appengine
from auth import Auth
from api_master import UrlMaster


class Firebase():
    def __init__(self, config) -> None:
        self.url_master = UrlMaster(config["apiKey"])
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
        return Auth(self.url_master, self.requests, self.credentials)
