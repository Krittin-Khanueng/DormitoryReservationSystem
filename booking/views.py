from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from dorm.models import Room
from .models import Booking


class BookingRoomView(View):
	def post(self, request):
		print(request.POST.get('room_id'))
		user = self.get_user(request.user.id)
		room = self.get_room(request.POST.get('room_id'))
		try:
			booking = Booking(room=room, user=user)
		except:
			pass
		booking.add_to_room()
		booking.save()
		return render(request, 'booking/booking_success.html')

	def get_room(self, room_id):
		room = Room.objects.get(room_id__exact=room_id, amount__gt=0, is_status=True)
		if room:
			return room
		return None

	def get_user(self, user_id):
		user = get_object_or_404(User, id=user_id)
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
