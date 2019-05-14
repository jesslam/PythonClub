from django.test import TestCase
from django.urls import reverse
from .models import Meeting, MeetingMinutes, Resource, Event
from django.contrib.auth.models import User



# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        m=Meeting(meetingtitle='hello')
        self.assertEqual(str(m), m.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        mm=MeetingMinutes(durationid='1')
        self.assertEqual(str(mm), mm.durationid)

    def test_table(self):  
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        r=Resource(resourcename='Stack Overflow')
        self.assertEqual(str(r), r.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

# Tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='cooldude'),
        self.mevent=Meeting.objects.create(meetingtitle='Best Meeting Ever', meetingdate='2019-04-20',
        meetingtime='12:00:00', meetinglocation='Cal Anderson')
        

    def test_meetings_test_success(self):
        response=self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)



