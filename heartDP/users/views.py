from django.shortcuts import render,redirect
from forms import RegisterForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method  == "POST":
        form = RegisterForm(request.post)
        if form.is_valid():
            User = form.save()
            login(request , User)
        else:
            form = RegisterForm()
        return render(request, "users/register.html", {"form":form})