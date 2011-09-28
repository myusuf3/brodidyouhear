from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'webcomic.views.index', name='home'),
     url(r'^comic/(?P<id>\d+)/$', 'webcomic.views.comic', name='game'),
     url(r'^random$', 'webcomic.views.random', name = 'random'),

    # Uncomment the admin/doc line below to enable admin documentation:
 	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
