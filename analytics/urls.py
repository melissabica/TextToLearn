from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns (' ',
	url(r'^$', views.analytics, name="analytics"),
)
