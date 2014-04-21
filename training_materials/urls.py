from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns (' ',
	url(r'^$', views.training_materials, name="training_materials"),
    url(r'^training_materials/add/$', views.training_materials_add, name="training_materials_add"),
    url(r'^(?P<pk>\d+)/edit/$', views.training_materials_add, name="training_materials_add"),
    url(r'^(?P<pk>\d+)/edit/quiz/$', views.training_materials_quiz, name="training_materials_quiz"),
    url(r'^(?P<pk>\d+)/preview/$', views.training_materials_preview, name="training_materials_preview"),
    url(r'^(?P<pk>\d+)/assign/$', views.training_materials_assign, name="training_materials_assign"),


)