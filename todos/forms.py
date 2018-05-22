from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['point_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['point_value'].label = 'Experience Points'

    class Meta:
        model = Todo
        fields = ('title', 'point_value')
