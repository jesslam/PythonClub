from django.test import TestCase
from django.urls import reverse
from .models import Meeting, MeetingMinutes, Resource, Event
from django.contrib.auth.models import User



# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='Northgate Meeting')
        self.assertEqual(str(type), type.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        type=MeetingMinutes(durationid='1')
        self.assertEqual(str(type), type.durationid)

    def test_table(self):  
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='Stack Overflow')
        self.assertEqual(str(type), type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


