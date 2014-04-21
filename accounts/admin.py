from django.contrib import admin
from accounts.models import PersonalData, RequestData

admin.site.register(PersonalData)
admin.site.register(RequestData)