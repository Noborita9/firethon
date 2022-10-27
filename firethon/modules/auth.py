from utils.request_master import RequestMaster


class Auth():
    def __init__(self, endpoint_master, requests, credentials) -> None:
        self.request_master = RequestMaster(endpoint_master, requests)
        self.credentials = credentials
        self.last_user = None

    def refresh_token(self, refresh_token):
        response = self.request_master.request(
            "refresh_token", {"refresh_token": refresh_token})
        return response

    def sign_in_with_email_and_password(self, email, password):
        response = self.request_master.request("sign_in_with_email_and_password", {
                                               "email": email, "password": password})
        self.last_user = response
        return response

    def sign_up_with_email_and_password(self, email, password):
        response = self.request_master.request("sign_up_with_email_and_password", {
                                               "email": email, "password": password})
        self.last_user = response
        return response

    def sign_in_anonymously(self):
        response = self.request_master.request("sign_in_anonymously", {})
        self.last_user = response
        return response
