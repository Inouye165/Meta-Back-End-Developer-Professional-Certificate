from django.shortcuts import render

# Create your views here.
def index(request, name):       
    context={'name': name}   
    person={'name':'Roger', 'profession':'Teacher'}
    return render(request, 'index.html', context) 

# The following code does not work because the index2 function does not accept any parameters.
# def index2(request):       
#     person = {'name': 'Roger', 'profession': 'Teacher'} 
#     return render(request, 'index.html', person)
def index2(request,name):  
    rate = 5
    interest = 5 * rate / 100  # Pe
    person = {'name': 'Roger', 'profession': 'Teacher'}
    langs =['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    courses = {
    'Mathematics': 30,
    'Science': 25,
    'History': 20,
}
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']} 

    context = {'person': person,
                'name':name,
                'user':'admin',
                'langs' : langs,
                'data': courses,
                'langs': langs,
                'dct': dct,
                'rate': rate,
                'interest': interest,
}  # Wrap the person dictionary in another dictionary
    return render(request, 'index.html', context)