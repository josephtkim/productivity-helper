from django.test import TestCase
from .models import Todo
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.
class TodoTest(TestCase):
    def create_Todo(self, title="test title", point_value=10):
        u = User(username="Tester", password="password")
        u.save()
        return Todo.objects.create(title=title, author=u, pub_date=timezone.now(), point_value=point_value, completed=False)

    # MODEL
    def test_Todo_creation(self):
        """Todo is correctly created"""
        test_todo = self.create_Todo()
        self.assertTrue(isinstance(test_todo, Todo))

    def test_Todo_title(self):
        """Title is the same as __str__ string"""
        test_todo = self.create_Todo()
        self.assertTrue(test_todo.title == str(test_todo))

    # FORMS
    def test_valid_form(self):
        """Form is valid"""
        test_todo = self.create_Todo()
        data = {'title': 'title', 'point_value': 10}
        form = TodoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Form is invalid"""
        test_todo = self.create_Todo()
        data = {'title': '', 'point_value': 10}
        form = TodoForm(data=data)
        self.assertFalse(form.is_valid())
