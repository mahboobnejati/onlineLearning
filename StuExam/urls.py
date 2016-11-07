from django.conf.urls import url
from . import views

app_StuExam = 'StuExam'

urlpatterns = [

    url(r'^$', views.DetailView.as_view() , name='index'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),
]


