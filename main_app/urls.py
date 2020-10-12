from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facts/', views.facts, name='facts'),
    path('accounts/<int:user_id>/', views.user_activities, name='user_activities'),
    path('activities/', views.ActivityList.as_view(), name='index'),
    path('activities/<int:activity_id>/', views.activities_detail, name='detail'),
    path('activities/<int:activity_id>/assoc_activity/<int:user_id>/', views.assoc_activity, name='assoc_activity'),
    path('activities/<int:activity_id>/unassoc_activity/<int:user_id>/', views.unassoc_activity, name='unassoc_activity'),
    path('accounts/signup/', views.signup, name='signup'),
]