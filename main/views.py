import hashlib
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio.twiml.messaging_response import MessagingResponse

from main.models import Recipient, Replies
from main.utils import *


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(get_context(request), request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render(get_context(request), request))


def authenticate(request):
    user = User.objects.get(username=request.POST.get('username'))
    hash = hashlib.sha256((request.POST.get('password') + user.salt).encode('utf-8')).hexdigest()
    for a in range(0, 4):
        hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
    if user.password == hash:
        request.session['userid'] = user.userid
        return redirect('/send')
    else:
        flash(request, 'Sorry an incorrect username or password was provided. Please try again.')
        return redirect('/login')


def logout(request):
    del request.session['userid']
    request.session.modified = True
    return redirect('/')


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render(get_context(request), request))


def enroll(request):
    recipient = Recipient(name=request.POST.get('name'), phone=request.POST.get('phone'), unit=request.POST.get('unit'),
                          group=request.POST.get('group'))
    recipient.save()
    send_text(recipient.phone, settings.INITIAL_TEXT)
    return redirect('/register')


def send(request):
    if not correct_permissions(request, 2):
        flash(request, 'Sorry, you do not have the correct permissions to perform this task.')
        return redirect('/')
    template = loader.get_template('send.html')
    return HttpResponse(template.render(get_context(request), request))


def dispatch(request):
    message = request.POST.get('message')
    recipients = Recipient.objects.all()
    for recipient in recipients:
        send_text(recipient.phone, message)
    print(get_groups(datetime.now().isoformat()))
    send_reciept(User.objects.get(userid=request.session['userid']).username, recipients, message)
    return redirect('/')


def replies(request):
    if not correct_permissions(request, 2):
        flash(request, 'Sorry, you do not have the correct permissions to perform this task.')
        return redirect('/')
    template = loader.get_template('replies.html')
    context = get_context(request)
    #    for reply in Replies.objects.all():

    #    context['phones'] =
    return HttpResponse(template.render(context, request))


@require_POST
@csrf_exempt
def incoming_message(request):
    resp = MessagingResponse()
    reply = Replies(phone=request.POST.get('From'), message=request.POST.get('Body'))
    reply.save()
    return HttpResponse(resp)
