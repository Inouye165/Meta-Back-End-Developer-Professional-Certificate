from django import forms
from myapp.models import Booking

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UserForm(NameForm):
    class Meta:
        model = Booking
        fields = "__all__"
        