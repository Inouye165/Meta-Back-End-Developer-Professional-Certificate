from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def pathview(request, name, id): 
    return HttpResponse("Pathview<br>Name:{} UserID:{}".format(name, id)) 
 
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Qryview<br>Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    return render(request, "form.html") 