# coding=utf-8
from accounts.models import RequestData


class RequestMiddleware(object):
    def process_request(self, request):
        r = RequestData()
        r.path = request.path
        r.method_request = request.method
        r.save()
