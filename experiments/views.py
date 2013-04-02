import datetime
import logging

from django.conf import settings
from django.utils import simplejson
from django.core.cache import cache
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify

from home.decorators import login_check
from lib.EchoNest import echo_get_artist, echo_lookup, echo_artist_info

logger = logging.getLogger('apps')

@login_check
def index(request):
    return render(request, 'index.html', locals())


@login_check
def music_search(request):
    main_search = echo_get_artist(request)
    search_key = slugify(main_search)

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

    return render(request, 'experiments/experiments.html', locals())
