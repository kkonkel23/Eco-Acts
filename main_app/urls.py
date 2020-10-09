from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facts/', views.facts, name='facts'),
    path('activities/', views.ActivityList.as_view(), name='activities_index'),
]