from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('add/', views.add_forum, name='add_forum'),
    path('post/<int:post_id>', views.forum_post, name='forum_post'),
    path('post/<int:post_id>/del/<int:msg_id>', views.comment_delete, name='comment_delete'),
]