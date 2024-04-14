# views.py in your demoapp

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404, render, redirect

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
def profile_view(request):
    print("Inside profile_view")
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        context = {'profile_user': user}
        return render(request, 'demoapp/profile.html', context)
    else:
        # Redirect to login or handle unauthenticated case
        return redirect('login')  # You'll need a login view