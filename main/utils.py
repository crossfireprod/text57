from django.conf import settings
from django.template import loader
from sendgrid.helpers.mail import *

from main.models import User


def correct_permissions(request, needed_permissions):
    if 'userid' not in request.session:
        return False
    else:
        user = User.objects.get(userid=request.session['userid'])
        if user is None:
            del request.session['userid']
            request.session.modified = True
            return False
        elif user.powerlevel < needed_permissions:
            return False
        else:
            return True


def send_text(phone, message):
    return settings.TWILIO_CLIENT.messages.create(
        to=phone,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=message)


def send_reciept(user, recipients, message):
    context = {'user': user,
               'cost': 0.0075 * len(recipients),
               'message': message}
    subject = "SMS Receipt"
    content = Content("text/html", loader.get_template('receipt.html').render(context))
    for email in settings.RECEIPT_RECIPIENTS:
        mail = Mail(settings.SENDGRID_FROM_EMAIL, subject, email, content)
        settings.SENDGRID_CLIENT.client.mail.send.post(request_body=mail.get())


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


def get_groups(date):
    groups = []
    for group in settings.GROUPS:
        if group[1] < date < group[2]:
            groups.append(group[0])
