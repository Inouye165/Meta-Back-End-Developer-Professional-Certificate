from django.shortcuts import render
from myapp.forms import LogForm

def form_view(request):
    form = LogForm() # Instance named form is created
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save() # This will save the data to the database
    return render(request, 'form.html', {'form': form})