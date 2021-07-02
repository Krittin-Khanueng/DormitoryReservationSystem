from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from dorm.models import Room
from .models import Booking


class BookingRoomView(View):
    def post(self, request):
        user = self.get_user(request)
        room = self.get_room(request)
        if room:  # เช็กว่าห้องเต็มแล้วหรือไหม
            booking, created = Booking.objects.get_or_create(room=room)
            if created:
                booking.save()
            if not user.account.is_booking_state:  # เช็กว่าผู้ใช้เคยจองห้องพักแล้วหรือไม
                # เอาผู้ใช้เข้าห้องพัก
                booking.user.add(user)
                booking.room.amount -= 1
                booking.room.save()
                booking.save()

                # เปลี่ยนสถานะการจองของผู้ใช้เป็นว่าจองแล้ว
                user.account.is_booking_state = True
                user.account.save()
                return render(request, 'booking/booking_success.html')

        else:
            messages.warning(
                request, 'ห้องพักที่คุณจองเต็มแล้ว กรุณาจองห้องใหม่')
            return HttpResponseRedirect(reverse("dorm"))

    def get_room(self, request):
        room = Room.objects.filter(room_id__exact=request.POST.get(
            'room_id'), amount__gt=0, is_status=True).first()
        if room:
            return room
        return None

    def get_user(self, request):
        user = get_object_or_404(
            User, id=request.user.id, account__is_booking_state=False)
        if user:
            return user
        return None


class ConfirmRoomView(View):
    def post(self, request):
        user = User.objects.get(id=request.user.id)
        room = Room.objects.get(id=request.POST.get('room_id'))
        context = {
            "room": room,
            "user": user
        }
        return render(request, 'booking/booking_confirm.html', context)
