import datetime
import logging

from django.http import HttpResponse, Http404

def login_check(func):
    ''' Check to see if the user is logged in '''
    def _call(request, *args, **kwargs):
        if request.user.is_authenticated():
            #print "authenticated user"
            pass
        else:
            # print "non-authenticated user"
            pass
        return func(request)
    return _call
