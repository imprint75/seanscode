import datetime
import logging

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import redirect, render, get_object_or_404

from home.decorators import login_check

def index(request):
    return render(request, 'work/work.html', locals())
