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
		if room:
			try:
				booking = Booking.objects.get(room=room)
			except:
				booking = Booking(room=room)
			booking.save()
			booking.user.add(user)
			booking.room.amount -= 1
			booking.room.save()
			booking.save()
			return render(request, 'booking/booking_success.html')
		else:
			messages.warning(request, 'หอพักที่คุณจองเต็มแล้ว กรุณาจองห้องใหม่')
			return HttpResponseRedirect(reverse("dorm"))

	def get_room(self, request):
		room = Room.objects.filter(room_id__exact=request.POST.get('room_id'), amount__gt=0, is_status=True).first()
		if room:
			return room
		return None

	def get_user(self, request):
		user = get_object_or_404(User, id=request.user.id)
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
