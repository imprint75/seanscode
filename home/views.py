import datetime
import logging

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from home.decorators import login_check

logger = logging.getLogger('apps')

@login_check
def index(request):
    return render_to_response('home.html',
                              locals(),
                              RequestContext(request))

@login_check
def info(request):
    message = "Info"
    return render_to_response('base.html',
                              locals(),
                              RequestContext(request))
