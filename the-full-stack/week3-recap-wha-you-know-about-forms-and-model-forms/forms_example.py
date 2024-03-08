from django import forms
from .model_sample import Logger
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        