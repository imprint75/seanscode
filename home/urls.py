from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('home.views',
    url(r'^/?$', 'index', name='home'),
)
