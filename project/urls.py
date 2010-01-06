from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

 	url(r'^$', include('ideum.urls')),
 	url(r'^idea/', include('ideum.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/(.*)', admin.site.root),

)


# Server static files through Django if on a development machine
if hasattr(settings, 'STATIC_FILE_LOCATION'):
	urlpatterns += patterns('',	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_FILE_LOCATION}), )
