from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'page/home.html',context)
