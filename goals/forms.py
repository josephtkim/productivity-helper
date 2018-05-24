from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label = 'Title'

        self.fields['point_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['point_value'].widget.attrs['min'] = 0
        self.fields['point_value'].label = 'Experience Points'

        self.fields['current_amount_done'].widget.attrs.update({'class': 'form-control'})
        self.fields['current_amount_done'].widget.attrs['min'] = 0
        self.fields['current_amount_done'].label = 'Current Progress'

        self.fields['amount_goal'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount_goal'].widget.attrs['min'] = 1
        self.fields['amount_goal'].label = 'Target Amount'

        self.fields['amount_per_increment'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount_per_increment'].widget.attrs['min'] = 1
        self.fields['amount_per_increment'].label = 'Increment'

        self.fields['units'].widget.attrs.update({'class': 'form-control'})
        self.fields['units'].label = 'Units'

    class Meta:
        model = Goal
        fields = ('amount_per_increment', 'title',
            'amount_goal', 'units',
            'point_value',
            'current_amount_done'
        )
