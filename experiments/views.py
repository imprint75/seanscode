import datetime
import logging
import urllib
import urllib2

from django.conf import settings
from django.utils import simplejson
from django.core.cache import cache
from django.core.context_processors import csrf
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from home.decorators import login_check
from lib.EchoNest import echo_get_artist, echo_lookup, echo_artist_info

logger = logging.getLogger('apps')

@login_check
def index(request):
    main_search = echo_get_artist(request)
    search_key = urllib2.quote(main_search.encode('utf8'))

    if cache.get(search_key):
        info = cache.get(search_key)
    else:
        info = {}
        details = echo_lookup(search_key)
        for i in details:
            blogs = echo_artist_info(i['id'], "blogs")
            blogs = blogs if blogs else ["No blogs found"]
            info[i['name']] = blogs

        cache.set(search_key, info, 60000)

    return render_to_response('experiments.html',
                              locals(),
                              RequestContext(request))
