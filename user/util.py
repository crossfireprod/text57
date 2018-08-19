
def quiet_logout(request):
    del request.session['userid']
    request.session.modified = True
