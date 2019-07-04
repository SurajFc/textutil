from django.shortcuts import render
from django.http import HttpResponse
from .models import mycontact
# Create your views here.
def contact(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        email = request.POST["email"]
        msg = request.POST["msg"]
        myc = mycontact(fname=fname,email=email,msg=msg)
        myc.save()
    return render (request,"contact.html")


def success(request):
    return HttpResponse("success")