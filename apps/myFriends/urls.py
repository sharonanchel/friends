from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
    url(r'^friends$', views.friends),
    # url(r'^friends/remove/(?P<id>\d+)$', views.user),
	url(r'^friends/create$', views.create),
	url(r'^user$', views.user),



]
