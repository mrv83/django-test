from django.shortcuts import render_to_response, get_object_or_404
from accounts.models import PersonalData, RequestData

def personal_data_output(request):
    me = get_object_or_404(PersonalData, pk=1)
    return render_to_response('content.html', {'me': me})

def requests_output(request):
    requests = RequestData.objects.all().order_by('-id')[:10]
    return render_to_response('requests.html', {'requests': requests})