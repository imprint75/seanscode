import datetime
import logging

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import redirect, render_to_response, get_object_or_404

from home.decorators import login_check

def index(request):
    return render_to_response('work.html',
                              locals())
