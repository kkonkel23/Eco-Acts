from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.BlogPostList.as_view(), name='blog'),
    path('blog/create/', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('blog/<int:blogpost_id>/', views.blogpost_detail, name='blogpost_detail'),
    path('accounts/<int:user_id>/', views.user_activities, name='user_activities'),
    path('activities/', views.activities_index, name='index'),
    path('activities/<int:activity_id>/', views.activities_detail, name='detail'),
    path('accounts/<int:user_id>/add_note', views.add_note, name='add_note'),
    path('accounts/<int:pk>/delete_note', views.NoteDelete.as_view(), name='delete_note'),
    path('accounts/<int:pk>/update_note', views.NoteUpdate.as_view(), name='note_update'),
    path('activities/<int:activity_id>/assoc_activity/<int:user_id>/', views.assoc_activity, name='assoc_activity'),
    path('activities/<int:activity_id>/unassoc_activity/<int:user_id>/', views.unassoc_activity, name='unassoc_activity'),
    path('accounts/signup/', views.signup, name='signup'),
]