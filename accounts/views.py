from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from accounts.models import PersonalData, RequestData
from accounts.forms import PersonalDataForm


def personal_data_output(request):
    me = get_object_or_404(PersonalData, pk=1)
    return render_to_response('content.html', {'me': me})


def requests_output(request):
    requests = RequestData.objects.all().order_by('-id')[:10]
    return render_to_response('requests.html', {'requests': requests})


@login_required
def personal_data_edit(request):
    me = get_object_or_404(PersonalData, pk=1)
    if request.method == 'POST':
        form = PersonalDataForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    #     else:
    #         form = PersonalDataForm(me)
    #         return render_to_response('edit.html', {'form': form})
    # else:
    #     form = PersonalDataForm(me)
    #     return render_to_response('edit.html', {'form': form})

    form = PersonalDataForm(me)
    return render_to_response('edit.html', {'form': form})