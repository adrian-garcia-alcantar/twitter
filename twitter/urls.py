from django.conf.urls.defaults import patterns, include, url
from registration.forms import RegistrationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^twitter/', include('twitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/register/$', 'registration.views.register',
                {'backend': 'registration.backends.default.DefaultBackend', 'form_class': RegistrationForm}),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
