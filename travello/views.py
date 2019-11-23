from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Destination
from accounts.views import login

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request,"index.html", {'dests' : dests})

def dest_redirect(request,destname):
    return render(request,"destination.html",{'dest' : destname})