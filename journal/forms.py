from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label = "Title"

        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].label = "Content"

    class Meta:
        model = Entry
        fields = ('title', 'content')
