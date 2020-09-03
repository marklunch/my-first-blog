from django.urls import path
from . import views

#patterns

urlpatterns = [
        path('', views.post_list, name='post_list'),
        ]
