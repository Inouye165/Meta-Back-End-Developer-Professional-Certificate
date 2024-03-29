from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = HttpResponse()
    response.headers['Age'] = 20
    
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    msg = f'''<br>
    <br>Path: {path}
    <br>Addres: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User Agent: {user_agent}
    <br>Path Info: {path_info}
    <br>Response.headers: {response.headers}
'''
    
    # response = HttpResponse('This works!')
    return HttpResponse(msg, content_type='text/html',charset='utf-8')