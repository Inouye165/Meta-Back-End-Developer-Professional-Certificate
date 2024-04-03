from django import forms
shifts = [
    ('1', 'Morning'),
    ('2', 'Evening'),
    ('3', 'Night'),
]
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    shift = forms.ChoiceField(choices=shifts)
    time_log = forms.TimeField(help_text='Enter the exact time')
    