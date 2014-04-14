
from accounts.models import Request_data

class RequestMiddleware(object):

  def process_request(self, request):
      r = Request_data()
      r.path = request.path
      r.method_request = request.method
      r.save()
