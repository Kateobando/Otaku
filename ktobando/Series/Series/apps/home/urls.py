from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Series.apps.home.views',
	url(r'^$','index_view', name ='vista_principal'),
	url(r'^login/$','login_view', name= 'vista_login'),
	url(r'^logout/$','logout_view', name= 'vista_logout'),
	url(r'^serie/(?P<id_prod>.*)/$', 'single_series_view', name = 'vista_single_series'),
	url(r'^series/page/(?P<pagina>.*)/$','series_view', name='vista_series'),
	url(r'^registro/$','register_view',name='vista_registro'),
	
)