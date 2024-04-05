#urls.py 

from django.urls import path
from . import views 
from myapp.views import EmployeeCreate, EmployeeSuccessView
from myapp.views import EmployeeList, EmployeeDetail, EmployeeUpdate
from myapp.views import EmployeeDelete
urlpatterns = [   
    # path('', IndexView.as_view(), name='index'),
    path('create/', views.EmployeeCreate.as_view(), name = 'EmployeeCreate')  ,
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete'), 
    path('list/', views.EmployeeList.as_view(), name = 'EmployeeList')  , 
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate') ,
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail') ,
    path('employees/success/', EmployeeSuccessView.as_view(), name='employee_success'),
]  