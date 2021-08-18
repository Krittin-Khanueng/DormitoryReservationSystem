from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from dorm.models import Room
from .models import Booking, Booking_confirmation




class BookingRoomView(View):
    def post(self, request):

        user = self.get_user_from_models(request)
        room = self.get_room_from_models(request)

        if user and room:  # เช็กว่าห้องเต็มแล้วหรือไหม
            booking, created = Booking.objects.get_or_create(room=room)
            if created:
                booking.save()
            if not user.account.is_booking_state:  # เช็กว่าผู้ใช้เคยจองห้องพักแล้วหรือไม
                return self.booking_room(booking, user)
        else:
            messages.warning(request, 'ห้องพักที่คุณจองเต็มแล้ว กรุณาจองห้องใหม่')
            return HttpResponseRedirect(reverse("dorm"))


    def booking_room(self, booking, user):
        #add user to booking

        booking.user = user
        booking.room.amount -= 1
        booking.room.save()
        booking.save()

        # เปลี่ยนสถานะการจองของผู้ใช้เป็นว่าจองแล้ว
        user.account.is_booking_state = True
        user.account.save()
        return HttpResponseRedirect(reverse('booking_success'))


    #get room from models where amount greater than 0
    def get_room_from_models(self, request):
        room = get_object_or_404(Room, id=request.POST.get('room_pk'), is_status=True, amount__gt=0)
        if room:
            return room
        return None

    def get_user_from_models(self, request):
        user = get_object_or_404(User, id=request.user.id, account__is_booking_state=False)
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

#get you for request

class BookingSuccessView(View):
    def get(self, request):
        return render(request, 'booking/booking_success.html')

#booking confirm
class ConfirmToBookView(View):
    def get(self, request):
        #get booking in current user
        booking = Booking.objects.filter(user_id=request.user.id).latest('booking_at')
        context = {
            "booking": booking
        }
        return render(request, 'booking/booking_confirm_to_book.html',context)
    
    
    def post(self, request):
        #get user from models

        #get booking in current user one objects

        booking = Booking.objects.filter(user_id=request.user.id).latest('booking_at')
        print(booking)
        data = request.POST.copy()
        
        if (data.get('is_confirmed') == 'true'):
            confirmation = Booking_confirmation(booking=booking, is_confirmed=True )
        else:
            confirmation = Booking_confirmation(booking=booking, is_confirmed=False )

        confirmation.save()
        return render(request, 'booking/booking_success.html')



class HistoryView(View):
    def get(self, request):
        
        bookings_list = Booking.objects.filter(user_id=request.user.id).order_by("-booking_at")
        context = {
            "bookings": bookings_list
        }
        
        return render(request, "booking/booking_history.html", context)
        
