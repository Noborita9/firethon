from constants import urls

class UrlMaster():
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.urls = {}

    def make_urls(self):
        for key, value in urls.items():
            new_data = value
            new_data["url"] = new_data["url"] + self.api_key
            self.urls[key] = new_data

    def get_services(self):
        return self.urls.keys()

    def get_service(self, service):
        return urls[service]
