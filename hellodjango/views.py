from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .settings import LOGIN_URL

def redirect_helper(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/shares/')
    else:
        return HttpResponseRedirect(LOGIN_URL)

@login_required
def shares(request):
    return render(request, 'shares.html')