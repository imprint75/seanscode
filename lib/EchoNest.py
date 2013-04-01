import datetime
import logging
import json
import urllib
import urllib2

from django.conf import settings
from django.utils import simplejson

def _make_call(options, *args, **kwargs):
    url = "{}{}/{}?api_key={}&name={}&format=json".format(settings.ECHO_NEST_BASE_URL,
                                                          options['type'],
                                                          options['action'],
                                                          settings.EN_API_KEY,
                                                          options['value'])

    jsonResponse = json.loads(urllib2.urlopen(url).read())

    if jsonResponse['response']['status']['message'] == "Success":
        return jsonResponse['response']
    else:
        return None


def echo_lookup(name = None, type = "artist"):
    results = _make_call({"type" : type,
                          "action" : "search",
                          "value" : name})
    return results[''.join([type, 's'])]


def echo_artist_info(id, method = "images"):
    results = _make_call({"type" : "artist",
                          "action" : method,
                          "value" : id})
    return results[method]


def echo_get_artist(request):
    try:
        return request.POST['artist_search']
    except:
        return settings.DEFAULT_ARTIST
