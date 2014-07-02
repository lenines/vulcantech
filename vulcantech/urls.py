from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', 'home.views.home', name='home'),
    url(r'^$', 'home.views.signin', name='signin'),
    url(r'^server1/', 'home.views.server1', name='server1'), 
    url(r'^server2/', 'home.views.server2', name='server2'),    
    url(r'^close_session/', 'home.views.close_session', name='close_session'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^task3/', 'scraping.views.get_categories', name='task3'),
    url(r'^owl/section/(?P<idcategory>\d+)/',
     'scraping.views.get_detail_categories', name='get_detail_categories'),    
    
)
