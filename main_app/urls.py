from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facts/', views.facts, name='facts'),
    path('accounts/signup/', views.signup, name='signup'),
    path('activities/', views.ActivityList.as_view(), name='index'),
    path('myactivities/', views.MyActivityList.as_view(), name='my_activities_index'),
    path('activities/<int:activity_id>/assoc_activity/<int:myactivity_id>/', views.assoc_activity, name='assoc_activity'),
]