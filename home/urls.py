from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('home.views',
    url(r'^home/', 'index', name='home'),
    url(r'^info/', 'info', name='home'),
)
