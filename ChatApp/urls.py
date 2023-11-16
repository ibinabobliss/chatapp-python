from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomescreen, name='FirstScreen'),
    path('home', views.HomePage, name='home'),
    path('<str:room_name>/<str:username>', views.message_room, name='room'),
]
