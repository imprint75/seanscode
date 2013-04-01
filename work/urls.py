from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('work.views',
    url(r'^/?$', 'index', name='home'),
)
