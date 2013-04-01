import logging
import requests

from django.conf import settings
from django.utils import simplejson

logger = logging.getLogger('apps')

def _make_call(options, *args, **kwargs):

    params = '&'.join(['api_key={}'.format(settings.EN_API_KEY),
                       'name={}'.format(options['value']),
                       'format=json'])

    r = requests.get('{}{}/{}?{}'.format(settings.ECHO_NEST_BASE_URL,
                                         options['type'],
                                         options['action'],
                                         params))
    res = r.json()

    if res['response']['status']['message'] == "Success":
        return res['response']
    else:
        return None


def echo_lookup(name = None, type_ = "artist"):
    results = _make_call({"type" : type_,
                          "action" : "search",
                          "value" : name})
    return results[''.join([type_, 's'])]


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
