from django.shortcuts import render , HttpResponse, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from accounts.forms import RegistrationForm , Edit_personal_details


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
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts')
#     else:
#         form = UserCreationForm()
#         args = {'form' : form}
#         return render(request, 'accounts/register.html', args)
#
# # custom_register.html
#
# def custom_register(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/user_profile')
#     else:
#         form = RegistrationForm()
#         args = {'form' : form}
#         return render(request, 'accounts/custom_register.html', args)
#
def user_profile(request):
    args = {'user' : request.user}
    return render(request, 'accounts/extract_user_data.html', args)
#
# def edit_user_profile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST,instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts')
#
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form' : form}
#         return render(request, 'accounts/edit_user_profile.html', args)
#
# def  Edit_personal_info(request):
#     if request.method == "POST":
#         form = Edit_personal_details(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts')
#     else:
#         form = Edit_personal_details(instance=request.user)
#         args = {'form': form}
#         return render(request,'accounts/edit_personal_info.html', args )

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

