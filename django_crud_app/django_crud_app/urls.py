from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^notes/', include('notes.urls', namespace="notes")),
    url(r'^admin/', include(admin.site.urls)),
)
