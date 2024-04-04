from django.shortcuts import render
from .forms import DemoForm

def form_view(request):
    form = DemoForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        print(name, email, message)
        return render(request, 'myapp/form_template.html', {'form': form})
    else:
        form = DemoForm()
    return render(request, 'myapp/form_template.html', {'form': form})


# Create your views here.
