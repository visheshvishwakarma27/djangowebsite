#from django.shortcuts import render,HttpResponse

# # Create your views here.
# def index(request):
#     return render(request,'index.html')
#     # return HttpResponse("this is home page")
# def about(request):
#     return HttpResponse("this is baout page")


# def news(request):
#     return HttpResponse("this is news page")

# def contact(request):
#     return HttpResponse("this is contact pagee")


# def services(request):
#     return HttpResponse("this is services page")

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')


def news(request):
    return render(request,'news.html')

def register(request):
    return render(request,'register.html')

def Contact(request):
    
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        subject=request.POST.get('subject')
        contact=Contact(firstname=firstname,lastname=lastname,Subject=subject,Date=datetime.today())
        contact.save()
    return render(request,'contact.html')


def services(request):
    return render(request,'services.html')


