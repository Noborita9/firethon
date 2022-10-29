from utils.request_master import RequestMaster

class Database():
    def __init__(self, endpoint_master, requester, credential) -> None:
        self.request_master = RequestMaster(endpoint_master=endpoint_master, requester=requester)
        self.credential = credential
        self.last_request = None
