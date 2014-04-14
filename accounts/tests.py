"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from models import PersonalData


class SimpleTest(TestCase):
    fixtures = ['personal_data.json']

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