from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),                  
    url(r'^', include('home.urls')),
    url(r'^', include('work.urls')),
    url(r'^', include('experiments.urls')),    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
