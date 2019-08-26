from django.conf.urls import url
from basic_app import views

#Create your urls here

#Template Tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^basic/$', views.basic, name='basic'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
