from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('nightout_user',

    #url(r'^$', 'views.home', name='home'),
    url(r'^$', 'views.promote', name='promote'),
    url(r'/promote$', 'views.promote', name='promote'),
    url(r'/promote_map*$', 'views.map', name='map'),
    url(r'/nightout_(.*)$', 'views.nightout', name='nightout'),
   	url(r'/tonight$', 'views.tonight', name='tonight'),
    url(r'/past$', 'views.past', name='past'),    
)