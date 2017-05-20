from django.test import TestCase
from django.contrib.auth.models import User


from .models import EVENT_KEY_RANDOM_COUNT, Event

class EventTestCase(TestCase):

    def setUp(self):

        self.fake_user_1 = User.objects.create(username='fake_user_1',
                                               email='fake_user_1@example.com',
                                               password='fake_user_1')
        self.fake_event_1 = Event()
        self.fake_event_1.owner = self.fake_user_1
        self.fake_event_1.save()

    def test_begin_not_none(self):
        """If begin is not set, datetimenow is set
        """
        self.assertIsNotNone(self.fake_event_1.begin)


    def test_key_not_none(self):
        """Key must be not none and not blank
        """
        self.assertIsNotNone(self.fake_event_1.key)
        self.assertNotEqual(self.fake_event_1.key, "")


    def test_key_length(self):
        """Key length must respect EVENT_KEY_RANDOM_COUNT value
        """
        self.assertEqual(len(self.fake_event_1.key), EVENT_KEY_RANDOM_COUNT)
