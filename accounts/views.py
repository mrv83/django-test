# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from accounts.models import PersonalData, RequestData, PRIORITY_CHOICES
from accounts.forms import PersonalDataForm, RegisterUser


def personal_data_output(request):
    me = get_object_or_404(PersonalData, pk=1)
    return render_to_response('content.html', {'me': me}, context_instance=RequestContext(request))


def requests_output(request):
    requests = RequestData.objects.all().order_by('-id')[:10]
    count_request = RequestData.objects.all().count()
    return render_to_response('requests.html',
                              {'requests': requests, 'choises': PRIORITY_CHOICES, 'count_request': count_request})


@login_required
def personal_data_edit(request):
    me = PersonalData.objects.get(pk=1)
    if request.method == 'POST':
        form = PersonalDataForm(request.POST, request.FILES, instance=me)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PersonalDataForm(instance=me)
            return render_to_response('edit.html', {'me': me, 'form': form}, context_instance=RequestContext(request))
    else:
        form = PersonalDataForm(instance=me)
        return render_to_response('edit.html', {'me': me, 'form': form}, context_instance=RequestContext(request))


def registration(request):
    if request.method == 'POST':
        form = RegisterUser(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RegisterUser()
    return render_to_response('registration.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def send_data(request):
    status = 'error'
    me = PersonalData.objects.get(pk=1)
    if request.is_ajax():
        form = PersonalDataForm(request.POST, request.FILES, instance=me)
        if form.is_valid():
            form.save()
            status = 'done'
    return HttpResponse(status)


def priority_request(request):
    if request.is_ajax():
        prior = request.POST.get('prior')
        if prior == 'all':
            requests = RequestData.objects.all().order_by('-id')[:10]
            count_request = RequestData.objects.all().count()
        else:
            requests = RequestData.objects.filter(priority=prior).order_by('-id')[:10]
            count_request = RequestData.objects.filter(priority=prior).count()
        return render_to_response('requests_load.html',
                                  {'requests': requests, 'choises': PRIORITY_CHOICES, 'count_request': count_request})