from django.shortcuts import render, redirect
from .forms import UserForm

def order(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Saves the booking directly
            return redirect('order_success')  # Redirect to a success page 
    else:
        form = UserForm()
    return render(request, 'forms.html', {'form': form})

def order_success(request):
    # Assuming a simple success message for now
    return render(request, 'myapp/success.html') 
