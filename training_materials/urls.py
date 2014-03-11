from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns (' ',
	url(r'^$', views.training_materials, name="training_materials"),
    url(r'^training_materials/add/$', views.training_materials_add, name="training_materials_add"),
    url(r'^(?P<pk>\d+)/edit/$', views.training_materials_add, name="training_materials_add"),
    url(r'^training_materials/remove/$', views.training_materials, name="training_materials_remove"),
    url(r'^training_materials/assign/$', views.training_materials, name="training_materials_assign"),


)