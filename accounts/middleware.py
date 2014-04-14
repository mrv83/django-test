import datetime


class RequestMiddleware(object):

  def process_request(self, request):
      now = datetime.datetime.now()
      print(request.path)
