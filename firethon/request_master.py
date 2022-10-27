import json


class RequestMaster():
    def __init__(self, endpoint_master, requester) -> None:
        self.endpoint_master = endpoint_master
        self.requester = requester

    def request(self, service, data):
        service = self.endpoint_master.get_service(service)
        request_target = service["url"]
        headers = service["headers"]
        data = json.dumps(data)
        request_object = self.requester.request(
            method=service["method"], url=request_target, headers=headers, data=data)
        response = request_object.json()
        return response
