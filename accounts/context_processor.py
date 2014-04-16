from django.conf import settings


def all_settings(request):
    return {'settings': settings}