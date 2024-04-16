"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from rest_framework import routers
from demoapp.views import UserViewSet, profile_view
from demoapp import views
from rest_framework import routers  
from demoapp.views import UserViewSet
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('__debug__/', include(debug_toolbar.urls)),
#     #path('', include('demoapp.urls')),
#     #path('', include('rest_framework.urls', namespace='rest_framework')),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include(router.urls)),   # Include the router's URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Re-add this line back
    path('accounts/profile/', profile_view, name='profile'),
]