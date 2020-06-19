
from .models import Empinsert
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from flask import Flask, request


# Create your views here.
def home(request):
    return render(request, 'home1.html')


#  return HttpResponse('hey1!!!!!!!!!!!!!!!!!')

def add_form(request):
    print("sucess")
    name = request.POST["name"]
    mail = request.POST["mail"]
    number = request.POST["number"]
    age = request.POST["age"]
    state = request.POST["state"]
    msg = request.POST["msg"]
    emp_insert = Empinsert(name=name, mail=mail, number=number, age=age, state=state, msg=msg)

    subject = 'Thank you for registration. we will text you soon'
    message = 'welcome to Modern driving training school'
    from_email = settings.EMAIL_HOST_USER
    to_list = [mail, settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    emp_insert.save()
    return render(request, 'home2.html')


