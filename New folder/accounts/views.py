from distutils.command.build_scripts import first_line_re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth 
# Create your views here.

def register(request):

    if request.method == "POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password1"]
        password=request.POST["password2"]


        if password1==password2:
            user=User.objects.create_user(username=username,password=password,email=email,firstname=firstname,lastname=lastname)

        user.save();
        print("user created")
        return redirect("/")







    return render(request,'register.html')
    