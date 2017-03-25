from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.profil, name='profil'),
     url(r'^kontakt/$', views.kontakt, name='kontakt'),
     url(r'^services/$', views.services, name='services'),
     url(r'^services/(?P<title>[-\w. ]+)/$', views.service_detail, name='service_detail'),
     url(r'^reward/$', views.reward, name='reward'),

]