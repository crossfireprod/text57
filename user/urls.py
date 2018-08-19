from django.urls import path

from . import views

urlpatterns = [
    path('users/login', views.login, name='login'),
    path('users/authenticate', views.authenticate, name='authenticate'),
    path('users/logout', views.logout, name='logout'),
    path('users/signup', views.signup, name='signup'),
    path('user/<slug:userid>', views.view_user, name='view_user'),
]