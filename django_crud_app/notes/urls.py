from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<note_id>\d+)/$', views.read, name='read')
)