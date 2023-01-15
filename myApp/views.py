from django.shortcuts import render, redirect
from myApp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
    
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pnumber=request.POST.get("pnumber")
        message=request.POST.get("message")
        myquery=Contact(name=name,email=email,phonenumber=pnumber,message=message)
        myquery.save()
        messages.info(request,"Thank you for your time..I will get back to you soon..")
    return redirect("/")

