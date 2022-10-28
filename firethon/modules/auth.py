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

    def sign_in_with_oauth_credential(self, request_uri, post_body):
        response = self.request_master.request("sign_in_with_oauth_credentials", {
                                               "requestUri": request_uri, "postBody": post_body})
        return response

    def fetch_email_providers(self, identifier, continue_uri):
        response = self.request_master.request("fetch_email_providers", {
                                               "identifier": identifier, "continueUri": continue_uri})
        return response

    def reset_password_with_email(self, email):
        response = self.request_master.request("reset_password_with_email", {
                                               "requestType": "PASSWORD_RESET", "email": email})
        return response

    def verify_password_reset_with_email(self, email):
        response = self.request_master.request(
            "verify_password_reset_with_email", {"email": email})
        return response

    def confirm_password_reset(self, email):
        response = self.request_master.request(
            "confirm_password_reset", {"email": email})
        return response
