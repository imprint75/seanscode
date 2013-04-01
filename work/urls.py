from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('work.views',
    url(r'^work/', 'index', name='home'),
)
