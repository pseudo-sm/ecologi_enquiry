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

    name = request.POST.get("name")
    email = request.POST.get("email").strip()
    company = request.POST.get("company")
    message = request.POST.get("message")
    body ="Name : "+name+"\nEmail : "+email+"\n company : "+company+"\nMessage : "+message
    email_msg = EmailMessage("Oscar consultancy enquiry", body, settings.EMAIL_HOST_USER, ["iprocop@oscarconsult.ro"])
    email_msg.send(fail_silently=False)
    return JsonResponse(True,safe=False)
