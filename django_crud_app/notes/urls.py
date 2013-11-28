from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<note_id>\d+)/$', views.read, name='read'),
	url(r'^(?P<note_id>\d+)/delete/$', views.delete, name='delete'),
	url(r'^create/$', views.create, name='create'),
)