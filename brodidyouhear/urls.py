from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


handler500 = 'webcomic.views.server_error'

urlpatterns = patterns('',
     url(r'^$', 'webcomic.views.index', name='index_comic'),
     url(r'^comic/(?P<id>\d+)/$', 'webcomic.views.comic', name='comic_view'),
     url(r'^about/', 'webcomic.views.about', name='about'),

    # Uncomment the admin/doc line below to enable admin documentation:
 	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 

if settings.DEBUG:
	urlpatterns	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
