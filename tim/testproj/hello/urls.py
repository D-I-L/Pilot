from django.conf.urls import patterns, url
from hello import views

urlpatterns = patterns('hello',
                       url(r'^$', views.greet, name='greet'),
                       )
