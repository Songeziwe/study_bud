from django.urls import path

from . import views

urlpatterns = [
  path('login/', views.loginView, name='login'),
  path('register/', views.registerView, name='register'),
  path('logout/', views.logoutUser, name='logout'),
  path('', views.home, name='home'),
  path('room/<str:pk>/', views.room, name='room'),
  path('create-room/', views.createRoom, name='create-room'),
  path('update-room/<str:pk>', views.updateRoom, name='update-room'),
  path('delete-room/<str:pk>', views.delete, name='delete-room'),
  path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
  path('profile/<str:pk>', views.userProfile, name='profile'),
  path('update-user/', views.updateUser, name='update-user'),
  path('topics/', views.topicsPage, name='topics'),
  path('activity/', views.activityPagae, name='activities')

]