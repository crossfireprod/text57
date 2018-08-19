import hashlib

from django.shortcuts import redirect, render

from user.util import quiet_logout
from .models import User


# Create your views here.

def signup(request):
    return render(request, 'user/login.html', {})


def login(request):
    return render(request, 'user/login.html', {})


def authenticate(request):
    user = User.objects.get(username=request.POST.get('username'))
    hash = hashlib.sha256((request.POST.get('password') + user.salt).encode('utf-8')).hexdigest()
    for a in range(0, 4):
        hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
    if user.password == hash:
        request.session['userid'] = user.userid
        return redirect('/send')
    else:
        return redirect('/login')


def logout(request):
    quiet_logout(request)
    return redirect('/')


def view_user():
    return redirect('')
