from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^entries/(?P<id>.*)/', views.entries, name='entries'), #([0-9]{4})/([0-9]{2})/ add data to url????
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about-me/', views.about, name='about')
]
