from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'contacts/', include('contacts.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 
admin.autodiscover()