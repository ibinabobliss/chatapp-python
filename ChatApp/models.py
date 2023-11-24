# models.py

from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.room_name}"
