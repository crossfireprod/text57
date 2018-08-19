import base64
import random

from django.shortcuts import render, redirect

from .util import *
from .models import Group


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html', {'orgs': get_orgs_information()})


def view_org(request, orgid):
    return render(request, 'dashboard/view_org.html', {**get_org_info(orgid), 'users': get_org_users(orgid)})


def send(request, orgid):
    return render(request, 'dashboard/send.html', get_org_info(orgid))


def dispatch(request, orgid):
    """message = request.POST.get('message')
    recipients = Recipient.objects.all()
    for recipient in recipients:
        send_text(recipient.phone, message)
    print(get_groups(datetime.now().isoformat()))
    send_reciept(User.objects.get(userid=request.session['userid']).username, recipients, message)"""
    return redirect('/')


def replies(request, orgid):
    context = get_org_info(orgid)
    context['numbers'] = get_org_replies(orgid).items()
    return render(request, 'dashboard/replies.html', context)


def groups(request, orgid):
    context = {**get_org_info(orgid), 'groups': get_org_groups(orgid)}
    print(context['groups'])
    return render(request, 'dashboard/groups.html', context)


def new_group(request, orgid):
    context = get_org_info(orgid)
    return render(request, 'dashboard/new_group.html', context)


def create_group(request, orgid):
    group = Group()
    group.name = request.POST.get('name')
    group.description = request.POST.get('description')
    print()
    group.active_window = request.POST.get('active-time-start') + "to" + request.POST.get('active-time-end')
    group.grpid = base64.b64encode(bytes([random.randint(0, 16777215)]))
    group.organization = Organization.objects.get(orgid=orgid)
    group.save()


def view_group(request, orgid, grpid):
    return render(request, 'dashboard/view_group.html', get_org_info(orgid))


def register(request):
    return render(request, 'dashboard/register.html', {})


def enroll(request):
    """recipient = Recipient(name=request.POST.get('name'), phone=request.POST.get('phone'), unit=request.POST.get('unit'),
                          group=request.POST.get('group'))
    recipient.save()
    send_text(recipient.phone, settings.INITIAL_TEXT)"""
    return redirect('/register')


def register_multiple(request):
    return render(request, 'dashboard/register.html', {})
