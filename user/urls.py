from django.urls import path

from . import views

urlpatterns = [
    path('users/login', views.login, name='login'),
    path('users/login/post', views.login_post, name='login_post'),
    path('users/logout', views.logout, name='logout'),
    path('users/signup', views.signup, name='signup'),
    path('users/signup/post', views.signup_post, name='signup_post'),
    path('user/<slug:userid>', views.view_user, name='view_user'),
]