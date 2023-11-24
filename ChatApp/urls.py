from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomescreen, name='FirstScreen'),
    path('<str:room_name>/<str:username>', views.message_room, name='room'),
    path('account',
         views.accountscreen, name='account'),
    path('home', views.HomePage, name='home'),
]
