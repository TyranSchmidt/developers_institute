from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('create/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('profile/cards', views.card_collection, name='card_collection'),
]