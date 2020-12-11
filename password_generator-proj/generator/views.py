from django.shortcuts import render
from django.http import HttpResponse
import random

def Home(request):
    return render(request, "generator/home.html")


def password(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    selpass = ''
    #num = int(request.Get.get('lenght')
    #num = int(request.Get.get("lenght"))
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    num = int(str(request.GET.get('lenght')))
    for i in range(num):
        selpass += chars[random.randint(0,len(chars)-1)]
    return render(request, "generator/password.html", {'password':selpass})

def about(request):
    return render(request, "generator/about.html")    
