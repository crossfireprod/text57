from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:orgid>', views.view_org, name='view_org'),
    path('<slug:orgid>/send', views.send, name='send'),
    path('<slug:orgid>/replies', views.replies, name='replies'),
    path('<slug:orgid>/groups', views.groups, name='groups'),
    path('<slug:orgid>/groups/new', views.new_group, name='new_group'),
    path('<slug:orgid>/groups/create', views.create_group, name='create_group'),
    path('<slug:orgid>/group/<slug:grpid>', views.view_group, name='view_group'),
]
