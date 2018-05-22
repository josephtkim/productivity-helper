from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class AccountTest(TestCase):
    def create_Account(self, level=1, experience_points=0):
        u = User(username="Tester", password="password")
        u.save()
        return Profile.objects.create(user=u, level=level, experience_points=experience_points)

    # MODEL
    def test_Profile_creation(self):
        """Entry is correctly created"""
        test_Profile = self.create_Account()
        self.assertTrue(isinstance(test_Profile, Profile))

    def test_gain_exp(self):
        """Gain experience points works as expected"""
        test_Profile = self.create_Account()
        test_Profile.gain_exp(110)

        self.assertTrue(test_Profile.level == 2)
        self.assertTrue(test_Profile.experience_points == 10)
