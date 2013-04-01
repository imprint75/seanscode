import logging

from django import template
from django.conf import settings
from django.template.context import RequestContext
from django.template.loader import render_to_string

register = template.Library()

@register.inclusion_tag('includes/menu.html')
def render_menu(request, categories=None):
    '''  This will generate the menu at the top  '''

    path = request.META['PATH_INFO']

    if path.startswith("/work"):
        path = '/info/'

    selected = ""

    pages = [
        { "page_title" : "Main", "link" : "home" },
        { "page_title" : "Music Search" , "link" : "experiments/music_search" },
        { "page_title" : "Work" , "link" : "work" },
        { "page_title" : "Info" , "link" : "info" }
    ]

    return {'pages' : pages,
            'request' : request,
            'selected' : selected}


@register.inclusion_tag('includes/list.html')
def render_list(request, items):
    return { "items" : items }
