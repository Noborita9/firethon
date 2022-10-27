import requests
import json from requests.adapters import HTTPAdapter import requests_toolbelt
import urllib3
from urllib3.contrib.appengine import is_appengine_sandbox
from requests_toolbelt.adapters import appengine



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
        return Auth(self.api_key, self.requests, self.credentials)


class Auth():
    def __init__(self, api_key, requests, credentials) -> None:
        self.api_key = api_key
        self.requests = requests
        self.credentials = credentials
        self.last_user = None

    def sign_in_with_email_and_password(self, email, password):
        act_request = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        headers = {"content-type": "application/json;"}
        data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
        request_object = self.requests.post(act_request, headers=headers, data=data)
        self.last_user = request_object.json()
        return self.last_user
