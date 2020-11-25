from django.shortcuts import render , HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
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

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.post)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts')
#     else:
#         form = UserCreationForm()
#         args = {'form' : form}
#         return render(request, 'accounts/register.html', args)

# custom_register.html

def custom_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
        args = {'form' : form}
        return render(request, 'accounts/custom_register.html', args)