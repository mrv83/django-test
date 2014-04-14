"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Personal_data, Request_data


class SimpleTest(TestCase):
    fixtures = ['personal_data.json']

    def test_data_found(self):
        me = Personal_data.objects.get(pk=1)
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
        me = Personal_data.objects.get(pk=1)
        self.assertEqual(response.context['me'], me)

class Request0Test(TestCase):
    fixtures = ['personal_data.json']

    def test_request_0(self):
        base_url = reverse('home')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 1)

class Request5Test(TestCase):
    fixtures = ['request_data_5.json', 'personal_data.json']

    def test_request_5(self):
        base_url = reverse('home')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 6) #with +1 requestwhen test called

class Request11Test(TestCase):
    fixtures = ['request_data_11.json', 'personal_data.json']

    def test_request_11(self):
        base_url = reverse('home')
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['requests']), 10)
        r = response.context['requests']
        r_first = r[0].id
        self.assertEqual(r_first, 12) #with +1 requestwhen test called