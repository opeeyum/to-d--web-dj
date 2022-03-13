from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("mainApp:index")
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, "accounts/login_register.html", context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect("mainApp:index")

    page_type = "login"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("mainApp:index")
        else:
            messages.error(request, "Invalid Credentials!")
    
    context = {'page_type': page_type}
    return render(request, "accounts/login_register.html", context)

def user_logout(request):
    logout(request)
    return redirect("mainApp:index")
