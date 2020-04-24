from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
#name,email,linkedin,subject,message
@csrf_exempt
def email_form(request):

    name = json.loads(request.POST.get("name"))
    email = json.loads(request.POST.get("email"))
    company = json.loads(request.POST.get("company"))
    message = json.loads(request.POST.get("message"))
    print(name,email,company,message)
    body ="Name : "+name+"\nEmail : "+email+"\n company : "+company+"\nMessage : "+message
    email_msg = EmailMessage("Oscar consultancy enquiry", body, settings.EMAIL_HOST_USER, ["saswathcommad@gmail.com"])
    email_msg.send(fail_silently=False)
    print(email_msg)
    return JsonResponse(True,safe=False)

def onelife(request):

    messaage = request.POST.get("message")
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    email_msg = EmailMessage("ecologi enquiry", messaage, settings.EMAIL_HOST_USER, ["ionut.procop.87@gmail.com"])
