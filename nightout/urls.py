from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

ROOT_URL = "nightout"

urlpatterns = patterns(ROOT_URL,
	url(r'^$', 'views.index', name='index'),
	url(r'^login$', 'views.login', name='login'),
	url(r'^user', include('nightout_user.urls')),
	url(r'^company', include('nightout_company.urls'))
	
)
