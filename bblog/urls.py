from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bblog.views.home', name='home'),
    url(r'^weblog/', include('weblog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)