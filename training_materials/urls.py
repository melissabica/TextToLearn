from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns (' ',
	url(r'^$', views.training_materials, name="training_materials"),
    url(r'^training_materials/add/$', views.training_materials, name="training_materials_add"),
    url(r'^training_materials/remove/$', views.training_materials, name="training_materials_remove"),

)