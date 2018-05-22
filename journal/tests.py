from django.test import TestCase
from .models import Entry
from .forms import EntryForm
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.
class EntryTest(TestCase):
    def create_Entry(self, title="test title", content="Some content"):
        u = User(username="Tester", password="password")
        u.save()
        return Entry.objects.create(title=title, author=u, published_date=timezone.now(), content=content)

    # MODEL
    def test_Entry_creation(self):
        """Entry is correctly created"""
        test_entry = self.create_Entry()
        self.assertTrue(isinstance(test_entry, Entry))

    def test_Entry_title(self):
        """Title is the same as __str__ string"""
        test_entry = self.create_Entry()
        self.assertTrue(test_entry.title == str(test_entry))

    def test_Entry_content_summary(self):
        """Length of summary is less than or equal to 400"""
        test_entry = self.create_Entry()
        summary = test_entry.show_summary()
        self.assertTrue(len(summary) <= 400)

    # FORMS
    def test_valid_form(self):
        """Form is valid"""
        test_entry = self.create_Entry()
        data = {'title': 'test title', 'content': 'content'}
        form = EntryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Form is invalid"""
        test_entry = self.create_Entry()
        data = {'title': 'test title', 'content': ''}
        form = EntryForm(data=data)
        self.assertFalse(form.is_valid())
