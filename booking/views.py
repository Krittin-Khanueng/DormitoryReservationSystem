from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from dorm.models import Room
from .models import Booking


class BookingRoomView(View):
    def post(self, request):
        user = self.get_user(request.user.id)
        room = self.get_room(request.POST.get('room_id'))
        if room:
            try:
                booking = Booking(room=room, user=user)
            except:
                pass
            booking.add_to_room()
            booking.save()
            # return render(request, 'booking/booking_success.html')
            return JsonResponse({"status": 'Success'})
        else:
            return JsonResponse({"status": 'ห้องเต็มแล้ว'})

    # get room

    def get_room(self, room_id):

        try:
            room = Room.objects.get(
                room_id__exact=room_id, amount__gt=0, is_status=True)
        except Room.DoesNotExist:
            room = None
        return room

    def get_user(self, user_id):
        user = get_object_or_404(User, id=user_id)
        if user:
            return user
        return None
