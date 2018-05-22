from django.test import TestCase
from .models import Goal
from .forms import GoalForm
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.
class GoalTest(TestCase):
    def create_Goal(self,
        title="test title",
        amount_goal=20,
        units = 1):
        u = User(username="Tester", password="password")
        u.save()
        return Goal.objects.create(
            title=title, amount_goal=amount_goal, units=units, author=u, pub_date=timezone.now(),
            point_value=50, current_amount_done=0, amount_per_increment=1, is_completed=False
        )

    def test_Goal_creation(self):
        """Entry is correctly created"""
        test_goal = self.create_Goal()
        self.assertTrue(isinstance(test_goal, Goal))

    def test_Goal_title(self):
        """Title is same as __str__ string"""
        test_goal = self.create_Goal()
        self.assertTrue(test_goal.title == str(test_goal))

    def test_Goal_increment(self):
        """Make sure increment method works"""
        test_goal = self.create_Goal()

        # increment by total goal. (Should be makred complete)
        # amount done is 1. goal is 10. increment is 10.
        # if incremented, amount done should be set equal to goal
        # and goal set as completed
        test_goal.current_amount_done = 1
        test_goal.amount_goal = 10
        test_goal.amount_per_increment = 10
        test_goal.increment()
        self.assertTrue(test_goal.current_amount_done == test_goal.amount_goal)
        self.assertTrue(test_goal.is_completed == True)

    def test_Goal_current_progress(self):
        """Make sure correct fraction for current progress method returned"""
        test_goal = self.create_Goal()
        test_goal.current_amount_done = 3
        test_goal.amount_goal = 11
        fraction = float(test_goal.current_amount_done) / test_goal.amount_goal
        fraction *= 100

        self.assertTrue(test_goal.current_progress() == round(fraction, 2))

    # FORMS
    def test_valid_form(self):
        """Form is valid"""
        test_goal = self.create_Goal()
        data = {'amount_per_increment': 1, 'title': 'title', 'amount_goal': 1,
        'units': 1, 'point_value': 50, 'current_amount_done': 1}

        form = GoalForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Form is invalid"""
        test_goal = self.create_Goal()
        data = {'amount_per_increment': 1, 'title': '', 'amount_goal': 1,
        'units': 1, 'point_value': 50, 'current_amount_done': 1}

        form = GoalForm(data=data)
        self.assertFalse(form.is_valid())
