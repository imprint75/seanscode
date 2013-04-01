from django.conf.urls import patterns, url, include

urlpatterns = patterns('experiments.views',
    url(r'^/?$', 'index', name='experiments.index'),
    url(r'^music_search/?$', 'music_search', name='experiements.music_search'),
)
