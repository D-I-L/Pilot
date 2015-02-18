from django.conf.urls import patterns, url
from readrender import views

urlpatterns = patterns('',
                       url(r'^$', views.welcome, name='welcome'),
                       url(r'^greet$', views.greet, name='greet'),
                       url(r'^read$', views.read_and_render, name='read_and_render'),
                      )
