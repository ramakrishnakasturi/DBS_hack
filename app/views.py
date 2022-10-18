from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from .forms import studentForm
from .models import Permission, Student,Lecturer
import smtplib
from email.message import EmailMessage
import pyautogui
import time
import pywhatkit
import datetime
from selenium.webdriver.common.keys import Keys

def login(request):
    if(request.method== "POST" ):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            global curr_user
            curr_user=username
            return render(request,"home.html",{curr_user:'curr'})
        else:
            message=""
            return render(request,"login.html",{message:"Invalid credentails"})
    else:
        return render(request,"login.html")
                