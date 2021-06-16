from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from dorm.models import Room
from .models import Booking


class BookingRoomView(View):
    def get(self, request, room_id):
        user = self.get_user(request.user.id)
        room = self.check_room(room_id)

        if room:
            try:
                booking = Booking(room=room, user=user)

            except:
                pass
            booking.add_to_room()
            booking.save()
        else:
            pass
        # room is Full
        return render(request, 'booking/booking_success.html')

    def check_room(self, room_id):
        room = get_object_or_404(Room, room_id__exact=room_id, amount__gt=0, is_status=True)
        if room:
            return room
        return None

    def get_user(self, user_id):
        user = get_object_or_404(User, id=user_id)
        if user:
            return user
        return None
