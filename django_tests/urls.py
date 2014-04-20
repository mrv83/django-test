# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'accounts.views.personal_data_output', name='home'),
                       url(r'^requests/$', 'accounts.views.requests_output', name='requests'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
                       url(r'^edit/$', 'accounts.views.personal_data_edit', name='edit'),
                       url(r'^registraion/$', 'accounts.views.registration', name='registration'),
                       url(r'^send_data/$', 'accounts.views.send_data', name='send_data'),
                       # Examples:
                       # url(r'^$', 'django_tests.views.home', name='home'),
                       # url(r'^django_tests/', include('django_tests.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()