import random

from django.conf import settings
from oanevsms.settings import B64_DIGITS
from django.template import loader
from sendgrid.helpers.mail import *


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
    content = Content("text/html", loader.get_template('main/receipt.html').render(context))
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
    """if 'userid' in request.session:
        context['username'] = User.objects.get(userid=request.session['userid']).username"""
    return context


def get_groups(date):
    groups = []
    for group in settings.GROUPS:
        if group[1] < date < group[2]:
            groups.append(group[0])


def convert_to_b64(int):
    result = ''
    while int:
        int, r = int // 64, int % 64
        result = B64_DIGITS[r] + result
    return result


def convert_from_b64(string):
    result = 0
    for digit in range(0, len(string)):
        result += B64_DIGITS.index(string[-digit - 1]) * 64 ** digit
    return result


def random_b64_number(length):
    result = ''
    for a in range(0, length):
        result += B64_DIGITS[random.randint(0, 64)]
    return result
