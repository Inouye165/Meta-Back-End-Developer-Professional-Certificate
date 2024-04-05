from django.views.generic.base import TemplateView 
from myapp.models import Employee
# class IndexView(TemplateView): 
#     template_name = 'index.html' 
from 
from django.views.generic.edit import CreateView , UpdateView , DeleteView 
from django.views.generic.detail import DetailView

class EmployeeCreate(CreateView):   
    model = Employee    
    fields = '__all__' 
    success_url = "/employees/success/" 
    
class EmployeeSuccessView(TemplateView):
    template_name = "myapp/employee_success.html"

from django.views.generic.list import ListView  
class EmployeeList(ListView):   
    model = Employee   
    success_url = "/employees/success/" 
    
class EmployeeDetail(DetailView):   
    model = Employee   
    success_url = "/employees/success/" 
    
from django.views.generic.edit import UpdateView  
class EmployeeUpdate(UpdateView):   
    model = Employee   
    fields = '__all__'   
    success_url = "/employees/success/" 
    
from django.views.generic.edit import DeleteView 
class EmployeeDelete(DeleteView):   
    model = Employee   
    success_url = "/employees/success/" 