from django.shortcuts import render, redirect 
from .forms import PersonForm

def form_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page (you'll create this later)
    else:
        form = PersonForm()
    return render(request, 'myapp/form.html', {'form': form})
from django.shortcuts import render

def success_view(request):
    return render(request, 'myapp/success.html')
