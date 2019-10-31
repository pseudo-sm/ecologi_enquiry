from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#name,email,linkedin,subject,message
@csrf_exempt
def email_form(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    linkedin = request.POST.get("linkedin")
    message = request.POST.get("message")
    subject = request.POST.get("subject")
    code = request.POST.get("code")
    body ="Name : "+name+"\nEmail : "+email+"\n Linkedin : "+linkedin+"\nSubject : "+subject+"\nMessage : "+message+"\n Code : "+code
    email_msg = EmailMessage("ecologi enquiry", body, settings.EMAIL_HOST_USER, ["ionut.procop.87@gmail.com"])
    email_msg.send(fail_silently=False)
    return JsonResponse(True,safe=False)

def onelife(request):

    messaage = request.POST.get("message")
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    email_msg = EmailMessage("ecologi enquiry", messaage, settings.EMAIL_HOST_USER, ["ionut.procop.87@gmail.com"])
