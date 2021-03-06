from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from account.models import Account
from account.views import Login_by_PSUPASSPORTView
from booking.forms import AccountForm
from booking.models import Opening_booking
from dorm.models import Room
from .models import Booking, Booking_confirmation


def get_opening_booking_from_models(group):
	opening_booking = Opening_booking.objects.filter(
		group=group, is_status=True).latest('created_at')
	if opening_booking:
		return opening_booking
	return None


def get_user_from_models(request):
	user = get_object_or_404(
		User, id=request.user.id, account__is_booking_state=False)
	if user:
		return user
	return None


def get_room_from_models(request):
	room = get_object_or_404(Room, id=request.POST.get(
		'room_pk'), is_status=True, amount__gt=0)
	if room:
		return room
	return None


class BookingRoomView(Login_by_PSUPASSPORTView, View):
	def post(self, request):

		user = get_user_from_models(request)
		room = get_room_from_models(request)
		group = self.get_group_from_models(request)
		opening_booking = get_opening_booking_from_models(group)

		if user and room:  # เช็กว่าห้องเต็มแล้วหรือไหม
			booking, created = Booking.objects.get_or_create(
				room=room, open_booking=opening_booking)
			if created:
				booking.save()
			if not user.account.is_booking_state:  # เช็กว่าผู้ใช้เคยจองห้องพักแล้วหรือไม
				return self.booking_room(booking, user)
		else:
			messages.warning(
				request, 'ห้องพักที่คุณจองเต็มแล้ว กรุณาจองห้องใหม่')
			return HttpResponseRedirect(reverse("dorm"))

	@staticmethod
	def booking_room(booking, user):
		# add user to booking

		booking.user = user
		booking.room.amount -= 1
		booking.room.save()
		booking.save()

		# เปลี่ยนสถานะการจองของผู้ใช้เป็นว่าจองแล้ว
		user.account.is_booking_state = True
		user.account.save()
		return HttpResponseRedirect(reverse('booking_success'))

	# get room from models where amount greater than 0

	@staticmethod
	def get_group_from_models(request):
		group = get_object_or_404(
			Group, id=request.user.groups.all()[0].id)
		if group:
			return group
		return None


class ConfirmRoomView(Login_by_PSUPASSPORTView, View):
	@staticmethod
	def post(request):
		user = User.objects.get(id=request.user.id)
		room = Room.objects.get(id=request.POST.get('room_id'))
		context = {
			"room": room,
			"user": user
		}
		return render(request, 'booking/booking_confirm.html', context)


class BookingSuccessView(Login_by_PSUPASSPORTView, View):
	@staticmethod
	def get(request):
		return render(request, 'booking/booking_success.html')


# booking confirm


class ConfirmToBookView(Login_by_PSUPASSPORTView, View):
	@staticmethod
	def get(request):
		# get booking in current user
		try:
			booking = Booking.objects.filter(
				user_id=request.user.id).latest('booking_at')
		except Booking.DoesNotExist:
			booking = None
		try:
			Booking_confirmation.objects.get(
				booking=booking, is_confirmed__isnull=False)
			msg = 'คุณได้ทำการยืนยันการจองห้องพักแล้ว'
			messages.success(request, msg)
			return HttpResponseRedirect(reverse('booking_success'))
		except Booking_confirmation.DoesNotExist:
			context = {
				"booking": booking
			}
			return render(request, 'booking/booking_confirm_to_book.html', context)

	def post(self, request):
		booking = Booking.objects.filter(
			user_id=request.user.id).latest('booking_at')
		data = request.POST.copy()
		if data.get('is_confirmed') == 'true':
			return self.save_booking_confirm(booking, True, 'booking_confirm_form')
		if data.get('is_confirmed') == 'false':
			return self.save_booking_confirm(booking, False, 'booking_success')

	@staticmethod
	def save_booking_confirm(booking, is_confirmed, redirect):
		confirmation = Booking_confirmation(
			booking=booking, is_confirmed=is_confirmed)
		confirmation.save()
		return HttpResponseRedirect(reverse(redirect))


class HistoryView(Login_by_PSUPASSPORTView, View):
	@staticmethod
	def get(request):
		bookings_list = Booking.objects.filter(
			user_id=request.user.id).order_by("-booking_at")
		context = {
			"bookings": bookings_list
		}

		return render(request, "booking/booking_history.html", context)


class ConfirmToBookFormView(Login_by_PSUPASSPORTView, View):
	@staticmethod
	def get(request):
		context = {
			"form": AccountForm()
		}
		return render(request, 'booking/booking_confirm_to_book_form.html', context)

	@staticmethod
	def post(request):
		# get account from models
		account = Account.objects.get(user_id=request.user.id)
		form = AccountForm(request.POST, request.FILES)
		if form.is_valid():
			account.image_profile = form.cleaned_data['image_profile']
			account.image_bill = form.cleaned_data['image_bill']
			account.save()
		# get data from request
		data = request.POST.copy()
		# get file form data

		account.motorcycle_registration = data.get('motorcycle_registration')
		account.car_registration = data.get('car_registration')
		account.phone_number = data.get('tel')
		account.bill_number = data.get('bill_number')
		# upload image to models
		account.save()

		return HttpResponseRedirect(reverse('index'))
