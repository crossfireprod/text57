
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio.twiml.messaging_response import MessagingResponse

from main.util import *


def index(request):
    return render(request, 'main/index.html', get_context(request))


"""@require_POST
@csrf_exempt
def incoming_message(request):
    resp = MessagingResponse()
    reply = Reply(phone=request.POST.get('From'), message=request.POST.get('Body'))
    reply.save()
    return HttpResponse(resp)"""
