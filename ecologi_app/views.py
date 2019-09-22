from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#name,email,linkedin,subject,message
@csrf_exempt
def email_form(request):
    body = ""
    email_msg = EmailMessage("ecologi enquiry", body, settings.EMAIL_HOST_USER, ["saswathcommand@gmail.com"])
    email_msg.send(fail_silently=False)
    return JsonResponse(True,safe=False)
