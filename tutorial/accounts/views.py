from django.shortcuts import render , HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is home page ")

def welcome(request):
    return render(request, 'accounts/welcome.html')

def passing_value(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Maaz'
    dictionary = {'myName' : name, 'numbers' : numbers}
    return  render(request, 'accounts/passing_value.html', dictionary )

def override(request):
    return render(request, 'accounts/override.html')