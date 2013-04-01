from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('experiments.views',
    url(r'^experiments/', 'index', name='home'),
)
