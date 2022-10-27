from constants import auth_endpoints


class EndpointMaster():
    def __init__(self, api_key, type) -> None:
        self.api_key = api_key
        self.urls = {}
        if type == "auth":
            self.make_urls(auth_endpoints)
        # Create database_endpoints
        elif type == "database":
            self.make_urls(auth_endpoints)
        # Create storage_endpoints
        elif type == "storage":
            self.make_urls(auth_endpoints)

    def make_urls(self, urls):
        for key, value in urls.items():
            new_data = value
            new_data["url"] = new_data["url"] + self.api_key
            self.urls[key] = new_data

    def get_services(self):
        return self.urls.keys()

    def get_service(self, service):
        return self.urls[service]
