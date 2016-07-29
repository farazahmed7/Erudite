from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.showSubjects, name='showSubjects'),
    	
]