from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import user,reservation
import smtplib
from email.message import EmailMessage
import pyautogui
import time
import pywhatkit
import datetime
from selenium.webdriver.common.keys import Keys

def home(request):
    return render(request,"home.html")
    
def book(request):
    if(request.method=="POST"):
        source=request.POST["source"]
        destination=request.POST["destination"]
        return render(request,"payments.html",{'source':source,'destination':destination})
    
    return render(request,"payments.html")

def pay(request):
    if request.method=="POST":
        email=request.POST["email"]
        subject="payment status"
        body="Your payment is succesfully done"
        to=email
        email_alert(subject,body,to)
    return render(request,"home.html")
    



def login(request):
    if(request.method== "POST" ):
        username=request.POST['username']
        password=request.POST['password']
        
        global curr_user
            curr_user=username
            return render(request,"home.html",{curr_user:'curr'})
        else:
            message=""
            return render(request,"login.html",{message:"Invalid credentails"})
    else:
        return render(request,"login.html")


def register(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        gender=request.POST['gender']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            t=user.objects.create(name=name,username=username,dept=dept,phno=phno,img=img,password=password1)
            t.save()
            return render(request,"login.html")
        else:
            return render(request,"register.html",{'message':'Passwords not matching'})
    return render(request,"register.html")


def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    

    user = "permisovnrvjiet@gmail.com"
    msg['from']= user
    password="yhagvyuhhfotjcaz"

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()