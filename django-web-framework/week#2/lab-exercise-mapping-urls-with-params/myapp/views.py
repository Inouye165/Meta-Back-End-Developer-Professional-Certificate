from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render
from datetime import datetime


# def index(request): 
#    return HttpResponse("Hello world! This is the index view of Myapp.") 

def pictures(request):
    return HttpResponse("pictures!")

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    response = HttpResponse()
    response.headers['age'] = 20

    msg = f"""<br>
        <br>Path:{path}
        <br>Address:{address}
        <br>Scheme:{scheme}
        <br>Method:{method}
        <br>User agent:{user_agent}
        <br>Path info:{path_info}
        <br> Response header: {response.headers}
        """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 

def say_hello(request):
    return HttpResponse("Another Hello World!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is the Little Lemon again!</h1>"""
    return HttpResponse(text)

def index(request):
    path = request.path
    method = request.method
    year = datetime.today().year
    content = """
    <center><h2>Testing Django Request Response Objects</h2>
    <p>The year is {}</p>
    <p>Request path : " {}"</p>
    <p>Request Method :{}</p></center>
    """.format(year, path, method)
    return HttpResponse(content)


def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request):
    return render(request, "form.html")

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(id, name)) 

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from ',
        'falafel': 'Falafel are deep fried patties or balls made from',
        'cheesecake': 'Cheescake is a type of dessert mad wwith '
        }
    description = items[dish]

    return HttpResponse(f"<h2>{dish} </h2>" + description)

def drinks(request,drink_name):
    drink = {
        'mocha':'type of coffee',
        'tea':'type of beverage',
        'water':'is good for you',
        'lemonade':'type of refreshment'
    }

    choice_of_drink = drink[drink_name]    
    return HttpResponse(f"<h2> {drink_name} is a {choice_of_drink}</h2>")
