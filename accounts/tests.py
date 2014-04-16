# coding=utf-8

import datetime

from accounts.middleware import RequestMiddleware

from django.test.client import RequestFactory

from django.test import TestCase
from django.core.urlresolvers import reverse
from models import PersonalData, RequestData

from django.conf import settings


class SimpleTest(TestCase):
    fixtures = ['initial_data.json']

    def test_data_found(self):
        me = PersonalData.objects.get(pk=1)
        self.assertEquals(me.pk, 1)
        self.assertEquals(me.name, "Viktor")
        self.assertEquals(me.surname, "Lysenko")
        self.assertEquals(me.date_of_birth, datetime.date(1983, 9, 7))
        self.assertEquals(me.bio, "Born, not dead yet")
        self.assertEquals(me.email, "lysenko.viktor.83@gmail.com")
        self.assertEquals(me.jabber, "mrv83@42cc.co")
        self.assertEquals(me.skype, "mrv830907")
        self.assertEquals(me.other_contact, "none")

    def test_url(self):
        base_url = reverse('home')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        me = PersonalData.objects.get(pk=1)
        self.assertEqual(response.context['me'], me)


class RequestTest(TestCase):
    fixtures = ['initial_data.json']

    def test_request_0_record_in_db(self):
        base_url = reverse('requests')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 1)

    def test_middleware(self):
        pre_count = RequestData.objects.all().count()
        self.factory = RequestFactory()
        self.middleware = RequestMiddleware()
        request = self.factory.get('/requests/')
        request.session = {}
        response = self.middleware.process_request(request)
        post_count = RequestData.objects.all().count()
        self.assertEquals(post_count, pre_count + 1)

    def test_request_5_record_in_db(self):
        for x in range(0, 5):
            r = RequestData()
            r.path = '/'
            r.method_request = 'GET'
            r.save()
        base_url = reverse('requests')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 6)  # with +1 request when test called

    def test_request_11_record_in_db(self):
        for x in range(0, 10):
            r = RequestData()
            r.path = '/'
            r.method_request = 'GET'
            r.save()
        base_url = reverse('requests')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 10)
        r = response.context['requests']
        r_first = r[0].id
        self.assertEqual(r_first, 11)  # with +1 request when test called        self.assertEqual(r_first, 12)  # with +1 request when test called


class TemplateContextProcessorTest(TestCase):
    fixtures = ['initial_data.json']

    def test_data_from_context_processor_exist(self):
        base_url = reverse('home')
        response = self.client.get(base_url)
        r = response.context['settings']
        self.assertEquals(r.TEMPLATE_CONTEXT_PROCESSORS, settings.TEMPLATE_CONTEXT_PROCESSORS)
        self.assertEquals(r, settings)