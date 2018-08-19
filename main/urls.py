from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('incoming_message', views.incoming_message, name='incoming_message'),
]