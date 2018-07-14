import hashlib

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from sendgrid.helpers.mail import *
from twilio.twiml.messaging_response import MessagingResponse

from main.models import User, Recipient, Replies


# Create your views here.

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
    message = settings.CLIENT.messages.create(
        to=recipient.phone,
        from_=settings.PHONE_NUMBER,
        body=settings.INITIAL_TEXT)
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
        text = settings.TWILIO_CLIENT.messages.create(
            to=recipient.phone,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=message)
    dispatch_receipt(User.objects.get(userid=request.session['userid']).username, recipients, message)
    return redirect('/')


def dispatch_receipt(user, recipients, message):
    context = {'user': user,
               'cost': 0.0075 * len(recipients),
               'message': message}
    subject = "SMS Receipt"
    content = Content("text/html", loader.get_template('receipt.html').render(context))
    for email in settings.RECEIPT_RECIPIENTS:
        mail = Mail(settings.SENDGRID_FROM_EMAIL, subject, email, content)
        settings.SENDGRID_CLIENT.client.mail.send.post(request_body=mail.get())


def replies(request):
    if not correct_permissions(request, 2):
        flash(request, 'Sorry, you do not have the correct permissions to perform this task.')
        return redirect('/')
    template = loader.get_template('replies.html')
    context = get_context(request)
    for reply in Replies.objects.all():

    context['phones'] =
    return HttpResponse(template.render(context, request))


@require_POST
@csrf_exempt
def incoming_message(request):
    resp = MessagingResponse()
    reply = Replies(phone=request.POST.get('From'), message=request.POST.get('Body'))
    reply.save()
    return HttpResponse(resp)


def correct_permissions(request, needed_permissions):
    if 'userid' not in request.session:
        return False
    else:
        user = User.objects.get(userid=request.session['userid'])
        if user is None:
            logout()
            return False
        elif user.powerlevel < needed_permissions:
            return False
        else:
            return True


def flash(request, message):
    request.session.modified = True
    if 'flashes' in request.session:
        request.session['flashes'].append(message)
    else:
        request.session['flashes'] = [message]


def get_context(request):
    context = {}
    if 'flashes' in request.session:
        context['flashes'] = request.session['flashes']
        del request.session['flashes']
        request.session.modified = True
    if 'userid' in request.session:
        context['username'] = User.objects.get(userid=request.session['userid']).username
    return context
