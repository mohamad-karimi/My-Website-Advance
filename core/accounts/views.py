from django.shortcuts import render
from .tasks import send_email_task
from django.http import HttpResponse


# Create your views here.
def send_email(request):
    send_email_task.delay()
    return HttpResponse("<h1>sending done</h1>")
