import datetime
import logging

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext

from home.decorators import login_check

logger = logging.getLogger(__name__)

@login_check
def index(request):
    return render(request, 'home.html', locals())

@login_check
def info(request):
    message = "Info"
    return render(request, 'common/base.html', locals())
