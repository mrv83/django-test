from django.shortcuts import render_to_response, get_object_or_404
from accounts.models import Personal_data

def personal_data_output(request):
    me = get_object_or_404(Personal_data, pk=1)
    return render_to_response('base.html', {'me': me})