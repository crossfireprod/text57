from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('enroll', views.enroll, name='enroll'),
    path('send', views.send, name='send'),
    path('dispatch', views.dispatch, name='dispatch'),
    path('replies', views.replies, name='replies'),
]