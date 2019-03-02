from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate, login,get_user_model

User = get_user_model()

def home_page(request):
    context = {
        "title " : "hello world",
        "content":"welcome to home page"
    }
    
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title " : "about world",
        "content":"welcome to about page"
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title " : "conatct world",
        "content":"welcome to contact page",
        "form": contact_form
    }
    # if contact_form.is_valid():

    return render(request,"contact/contact_page.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("/login")
        else:
            print("Error")


    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        
    return render(request, "auth/register.html",context) 
   