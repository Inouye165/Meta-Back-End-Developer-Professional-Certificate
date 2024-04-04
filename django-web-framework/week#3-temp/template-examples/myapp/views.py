from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 


# def index(request, name): 
#     return HttpResponse("<h1>Hello, {}. </h1>".format(name)) 
# from django.template import loader 
# def index(request): 
#     template = loader.get_template('hello.html') 
#     context={} 
#     return HttpResponse(template.render(context, request)) 

# from django.shortcuts import render 

# def index(request):
#     return render(request, 'hello.html', {}) 

from django.shortcuts import render  
def index(request, name):  
    context={"name":name}  
    return render(request, 'hello.html', context) 