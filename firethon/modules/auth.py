from utils.request_master import RequestMaster


class Auth():
    def __init__(self, endpoint_master, requests, credentials) -> None:
        self.request_master = RequestMaster(endpoint_master, requests)
        self.credentials = credentials
        self.last_user = None

    def refresh_token(self, refresh_token):
        response = self.request_master.request(
            "refresh_token",
            {"refresh_token": refresh_token})
        return response

    def sign_in_with_email_and_password(self, email, password):
        response = self.request_master.request(
            "sign_in_with_email_and_password",
            {"email": email, "password": password})
        self.last_user = response
        return response

    def sign_up_with_email_and_password(self, email, password):
        response = self.request_master.request(
            "sign_up_with_email_and_password",
            {"email": email, "password": password})
        self.last_user = response
        return response

    def sign_in_anonymously(self):
        response = self.request_master.request("sign_in_anonymously", {})
        self.last_user = response
        return response

    def sign_in_with_oauth_credential(self, request_uri, post_body):
        response = self.request_master.request(
            "sign_in_with_oauth_credentials",
            {"requestUri": request_uri, "postBody": post_body})
        return response

    def fetch_email_providers(self, identifier, continue_uri):
        response = self.request_master.request(
            "fetch_email_providers",
            {"identifier": identifier, "continueUri": continue_uri})
        return response

    def reset_password_with_email(self, email):
        response = self.request_master.request(
            "reset_password_with_email",
            {"requestType": "PASSWORD_RESET", "email": email})
        return response

    def verify_password_reset_with_email(self, oob_code):
        response = self.request_master.request(
            "verify_password_reset_with_email",
            {"oobCode": oob_code})
        return response

    def confirm_password_reset(self, oob_code, new_password):
        response = self.request_master.request(
            "confirm_password_reset",
            {"oobCode": oob_code, "newPassword": new_password})
        return response

    def change_email(self, id_token, email):
        response = self.request_master.request(
            "change_email",
            {"idToken": id_token, "email": email, "returnSecureToken": True})
        return response

    def change_password(self, id_token, password):
        response = self.request_master.request(
            "change_password",
            {"idToken": id_token, "password": password, "returnSecureToken": True})
        return response

    def update_profile(self, id_token, display_name, photo_url, delete_attribute):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token, "displayName": display_name, "photoUrl": photo_url, "returnSecureToken": True})
        return response

    def get_user_data(self, id_token):
        response = self.request_master.request(
            "get_user_data",
            {"idToken": id_token})
        return response

    def link_with_email_and_password(self, id_token, email, password):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token, "email": email, "password": password, "returnSecureToken": True})
        return response

    def link_with_oauht_credential(self, id_token, request_uri, post_body, return_credentials):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token, "requestUri": request_uri, "postBody": post_body, "returnSecureToken": True})
        return response

    def unlink_provider(self, id_token, delete_provider):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token, "deleteProvider": delete_provider})
        return response

    def send_email_verification(self, id_token):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token, "requestType": "VERIFY_MAIL"})
        return response

    def confirm_email_verification(self, oob_code):
        response = self.request_master.request(
            "update_profile",
            {"oobCode": oob_code})
        return response

    def delete_account(self, id_token):
        response = self.request_master.request(
            "update_profile",
            {"idToken": id_token})
        return response
