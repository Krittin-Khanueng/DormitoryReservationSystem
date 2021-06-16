import uuid

from django.contrib.auth.models import User
from django.db import models
from dorm.models import Room


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, related_name='booking_room')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ชื่อ:{self.user} {self.room}"

    def add_to_room(self):
        self.room.amount -= 1
        self.room.save()
