from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('nightout_company',

    url(r'^$', 'views.home', name='home'),
    url(r'/edit_establishment$', 'views.editEstablishment', name='editEstablishment'),
    url(r'/edit_location$', 'views.editLocation', name='editLocation'),
    url(r'/edit_event$', 'views.editEvent', name='editEvent'),
    url(r'/view_(.*)_events$', 'views.viewEvents', name='viewEvents'),
    url(r'/promote$', 'views.promote', name='promote'),
    url(r'/promote_(.*)$', 'views.promote', name='promote'),
    
)