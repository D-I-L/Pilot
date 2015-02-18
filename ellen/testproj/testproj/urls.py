from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('HelloWorld.urls')),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^HelloWorld/', include('HelloWorld.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
