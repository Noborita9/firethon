import json


class Auth():
    def __init__(self, url_master, requests, credentials) -> None:
        self.url_master = url_master
        self.requests = requests
        self.credentials = credentials
        self.last_user = None

    def sign_in_with_email_and_password(self, email, password):
        service = self.url_master.get_service(
            "sign_in_with_email_and_password")
        request_target = service["url"]
        headers = service["headers"]
        data = json.dumps(
            {"email": email, "password": password, "returnSecureToken": True})
        request_object = self.requests.request(
            method=service["method"], url=request_target, headers=headers, data=data)
        self.last_user = request_object.json()
        return self.last_user

    def sign_up_with_email_and_password(self, email, password):
        service = self.url_master.get_service(
            "sign_up_with_email_and_password")
        request_target = service["url"]
        headers = service["headers"]
        data = json.dumps(
            {"email": email, "password": password, "returnSecureToken": True})
        request_object = self.requests.request(
            method=service["method"], url=request_target, headers=headers, data=data)
        self.last_user = request_object.json()
        return self.last_user

    def refresh_token(self, refresh_token):
        service = self.url_master.get_service("refresh_token")
        request_target = service["url"]
        headers = service["headers"]
        data = json.dumps(
            {"refresh_token": refresh_token, "grant_type": "refresh_token"})
        request_object = self.requests.request(
            method=service["method"], url=request_target, headers=headers, data=data)
        refresh_token = request_object.json()
        return refresh_token


