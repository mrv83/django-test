# coding=utf-8
import datetime
import sys

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django.template import Template, Context
from django.test.client import RequestFactory
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from accounts.context_processor import all_settings
from accounts.forms import PersonalDataForm
from accounts.middleware import RequestMiddleware
from models import PersonalData, RequestData, DBAction, PRIORITY_CHOICES


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
        self.assertEqual(r_first, 11)  # with +1 request when test called


class TemplateContextProcessorTest(TestCase):
    fixtures = ['initial_data.json']

    def test_data_from_context_processor_exist(self):
        self.factory = RequestFactory()
        request = self.factory.get('/')
        context = all_settings(request)
        self.assertEquals(context['settings'], settings)
        self.assertTrue("accounts.context_processor.all_settings" in settings.TEMPLATE_CONTEXT_PROCESSORS)


class RegistrationTest(TestCase):
    fixtures = ['initial_data.json']

    def test_secure_page(self):

        self.user = User.objects.create_user('test', password='test')
        base_url = reverse('home')
        login_link = reverse('login')
        logout_link = reverse('logout')
        edit_link = reverse('edit')

        login = self.client.login(username='test', password='test')
        self.assertTrue(login)
        response = self.client.get(base_url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, login_link)
        self.assertContains(response, logout_link)
        self.assertContains(response, edit_link)
        logout = self.client.logout()
        response = self.client.get(base_url)
        self.assertContains(response, login_link)
        self.assertNotContains(response, logout_link)
        self.assertNotContains(response, edit_link)

    def test_form(self):
        self.user = User.objects.create_user('test', password='test')
        login = self.client.login(username='test', password='test')
        edit_link = reverse('edit')
        me = PersonalData.objects.get(pk=1)
        me_dict = me.__dict__
        form = PersonalDataForm(data=me_dict)
        response = self.client.post(edit_link, {'form': form})
        self.assertEquals(response.status_code, 200)

        for k in ["name", "surname", "bio", "skype", "other_contact", "userpic"]:
            me = PersonalData.objects.get(pk=1)
            me_dict = me.__dict__
            me_dict[k] = 'aaa111'
            form = PersonalDataForm(data=me_dict)
            self.assertTrue(form.is_valid())
        for k in ["email", 'jabber']:
            me = PersonalData.objects.get(pk=1)
            me_dict = me.__dict__
            me_dict[k] = 'viktor.83@gmail.com'
            form = PersonalDataForm(data=me_dict)
            self.assertTrue(form.is_valid())
        for k in ["name", "surname"]:
            me = PersonalData.objects.get(pk=1)
            me_dict = me.__dict__
            me_dict[k] = ''
            form = PersonalDataForm(data=me_dict)
            self.assertFalse(form.is_valid())
        for k in ["email", "jabber"]:
            me = PersonalData.objects.get(pk=1)
            me_dict = me.__dict__
            me_dict[k] = 'aaa'
            form = PersonalDataForm(data=me_dict)
            self.assertFalse(form.is_valid())


class CalendarTest(TestCase):
    fixtures = ['initial_data.json']

    def test_ajax_request(self):
        self.user = User.objects.create_user('test', password='test')
        login = self.client.login(username='test', password='test')
        edit_link = reverse('send_data')
        me = PersonalData.objects.get(pk=1)
        me_dict = me.__dict__
        form = PersonalDataForm(data=me_dict)
        response = self.client.post(edit_link, {'form': form})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'error')


class TagTest(TestCase):
    fixtures = ['initial_data.json']

    def test_tag_in_page(self):
        login = self.client.login(username='admin', password='admin')
        edit_link = reverse('edit')
        me = PersonalData.objects.get(pk=1)
        me_dict = me.__dict__
        form = PersonalDataForm(data=me_dict)
        response = self.client.post(edit_link, {'form': form})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '/admin/accounts/personaldata/1/')

    def test_tag(self):
        me = PersonalData.objects.get(pk=1)
        t = Template('{% load admin_edit %} {% admin_edit me %}')
        c = Context({'me': me})
        self.assertTrue(t.render(c).find('/admin/accounts/personaldata/1/') > -1)


class CommandTest(TestCase):
    class Output():

        def __init__(self):
            self.text = ''

        def write(self, string):
            self.text = self.text + string

        def writelines(self, lines):
            for line in lines:
                self.write(line)

    def test_db_out_command(self):

        command = "db_info"
        saved_streams = sys.stdout, sys.stderr

        sys.stdout = self.Output()
        sys.stderr = self.Output()
        has_errors = False

        try:
            call_command(command)
        except:
            has_errors = True

        self.assertFalse(has_errors)

        self.assertTrue(sys.stdout.text != "")
        self.assertTrue(sys.stderr.text == "")

        sys.stdout, sys.stderr = saved_streams

    def test_db_out_command_with_stderr(self):

        command = "db_info"
        saved_streams = sys.stdout, sys.stderr

        sys.stdout = self.Output()
        sys.stderr = self.Output()
        has_errors = False

        try:
            call_command(command, stderr=True)
        except:
            has_errors = True

        self.assertFalse(has_errors)

        valid_stdout = ''
        valid_stderr = ''

        for table in ContentType.objects.all():
            name = str(table)
            count = str(table.model_class().objects.count())
            row = 'Table: ' + name + '  object count: ' + count + '\n'
            valid_stdout += row
            row_e = 'error: ' + row
            valid_stderr += row_e

        self.assertTrue(sys.stdout.text != "")
        self.assertTrue(sys.stderr.text != "")

        self.assertEquals(sys.stdout.text, valid_stdout)
        self.assertEquals(sys.stderr.text, valid_stderr)

        sys.stdout, sys.stderr = saved_streams


class SignalTest(TestCase):
    fixtures = ['initial_data.json']

    def test_create_signal(self):
        log_pre_count = DBAction.objects.all().count()
        me = PersonalData.objects.get(pk=1)
        me.pk = 2
        me.save()
        log_post_count = DBAction.objects.all().count()
        self.assertTrue(log_post_count == log_pre_count + 1)
        self.assertTrue(DBAction.objects.get(pk=log_post_count).action_name == 'created')

    def test_change_signal(self):
        log_pre_count = DBAction.objects.all().count()
        me = PersonalData.objects.get(pk=1)
        me.name = 'aaa'
        me.save()
        log_post_count = DBAction.objects.all().count()
        self.assertTrue(log_post_count == log_pre_count + 1)
        self.assertTrue(DBAction.objects.get(pk=log_post_count).action_name == 'edited')

    def test_delete_signal(self):
        log_pre_count = DBAction.objects.all().count()
        me = PersonalData.objects.get(pk=1)
        me.delete()
        log_post_count = DBAction.objects.all().count()
        self.assertTrue(log_post_count == log_pre_count + 1)
        self.assertTrue(DBAction.objects.get(pk=log_post_count).action_name == 'deleted')


class RequestsLoadTest(TestCase):

    def test_templates(self):
        t = Template('requests_load.html')
        requests = RequestData.objects.all()
        count_request = 0
        c = Context({'requests': requests, 'choises': PRIORITY_CHOICES, 'count_request': count_request})
        self.assertTrue(t.render(c).find('Request with this priority not found') > -1)

        t = Template('selector.html')
        for x in range(0, 5):
            r = RequestData()
            r.path = '/'
            r.method_request = 'GET'
            r.priority = 1
            r.save()
        requests = RequestData.objects.all()
        count_request = 5
        c = Context({'requests': requests, 'choises': PRIORITY_CHOICES, 'count_request': count_request})
        self.assertTrue(t.render(c).find('load_requests') > -1)

