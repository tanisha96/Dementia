from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^eegsignalform/$', views.EegSignalForm, name='eegsignalform'),
    url(r'^eegsignal/$', views.EegSignal, name='eegsignal'),
    url(r'^eegsignal/symptomsform/$', views.SymptomsForm, name='symptomsform'),
    url(r'^eegsignal/symptoms/(?P<send>[0-9]+)/$', views.Symptoms, name='symptoms'),
    url(r'^eegsignal/result/(?P<slowing>([0-9]*[.])?[0-9]+)/(?P<age>([0-9]*[.])?[0-9]+)/(?P<ml>([0-9]*[.])?[0-9]+)/(?P<difii>([0-9]*[.])?[0-9]+)/(?P<mspeech>([0-9]*[.])?[0-9]+)/(?P<b>([0-9]*[.])?[0-9]+)/(?P<vh>([0-9]*[.])?[0-9]+)/(?P<result>([0-9]*[.])?[0-9]+)/$', views.results, name='results'),
    url(r'^deleteObject/$', views.deleteObject, name='deleteObject'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^dashboard/$', views.Login_user, name='login_user'),
    url(r'^dashboard2/$', views.getreg, name='signup_user'),
    url(r'^dashboard3/$', views.display, name='view_records_all'),
    url(r'^dashboard4/$', views.display1, name='view_history'),

]

