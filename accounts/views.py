from django.shortcuts import render_to_response, get_object_or_404
from accounts.models import Personal_data
from django_tests.settings import STATIC_ROOT

def personal_data_output(request):
    # me = Personal_data.objects.get(pk=1)
    me = get_object_or_404(Personal_data, pk=1)
    # print(STATIC_ROOT)
    return render_to_response('base.html', {'me': me})