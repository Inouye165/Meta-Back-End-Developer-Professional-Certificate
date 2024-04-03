from django import forms
from django.forms.widgets import NumberInput
fav_dish = [('pizza', 'Pizza'), ('pasta', 'Pasta'), ('salad', 'Salad')] 
class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label='Enter email address', max_length=100)
    email1 = forms.EmailField()
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea)  
    favorite_dish = forms.ChoiceField(widget=forms.RadioSelect, choices=fav_dish) 
    favorite_dish1 = forms.ChoiceField(choices=fav_dish) 