from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import Group, User
from booking.models import Opening_booking, Booking, Booking_confirmation, Academic_year
from dorm.models import Dormitory, Room
from .forms import DormitoryForm, FloorForm, RoomForm, Opening_bookingForm


def paginate_list(request, list, num):
    paginator = Paginator(list, num)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        list = paginator.page(paginator.num_pages)
    return list


class administerView(View):
    @staticmethod
    def get(request):
        return render(request, "administer/base_admin_page.html")


class administerdashboardView(View):
    @staticmethod
    def get(request):
        return render(request, "administer/dashboard.html")


class administerdorm_addView(View):
    @staticmethod
    def get(request):
        dorms = Dormitory.objects.all()
        dormPage = paginate_list(request, dorms, 3)

        context = {
            "form": DormitoryForm(),
            "dorms": dormPage,

        }
        return render(request, "administer/dorm/dorm_management_add.html", context)

    @staticmethod
    def post(request):
        form = DormitoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("management_dorm_add"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/dorm_management_add.html", context)


class administerdorm_editView(View):
    @staticmethod
    def get(request, id):
        dorm = Dormitory.objects.get(id=id)
        context = {
            "form": DormitoryForm(instance=dorm),
            "dorm": dorm
        }
        return render(request, "administer/dorm/dorm_management_edit.html", context)

    @staticmethod
    def post(request, id):
        dorm = Dormitory.objects.get(id=id)
        form = DormitoryForm(request.POST, request.FILES, instance=dorm)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("management_dorm_add"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/dorm_management_edit.html", context)


class administerdorm_deleteView(View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        dorm = Dormitory.objects.get(id=id)
        dorm.delete()
        return JsonResponse({"status": 'success'})


class administerdormView(View):
    @staticmethod
    def get(request):
        return render(request, "administer/dorm/dorm_management.html")


class administerfloor_addView(View):
    @staticmethod
    def get(request):
        context = {
            "form": FloorForm(),
        }
        return render(request, "administer/dorm/floor/floor_management_add.html", context)

    @staticmethod
    def post(request):
        form = FloorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("management_floor_add"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/floor/floor_management_add.html", context)


class administerroom_addView(View):
    @staticmethod
    def get(request):
        rooms = Room.objects.all()
        roomPage = paginate_list(request, rooms, 3)

        context = {
            "form": RoomForm(),
            "rooms": roomPage
        }
        return render(request, "administer/dorm/room/room_management_add.html", context)

    @staticmethod
    def post(request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("management_room_add"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/room/room_management_add.html", context)


class administerroom_editView(View):
    @staticmethod
    def get(request, id):
        room = Room.objects.get(id=id)
        context = {
            "form": RoomForm(instance=room),
        }
        return render(request, "administer/dorm/room/room_management_edit.html", context)

    @staticmethod
    def post(request, id):
        room = Room.objects.get(id=id)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("management_room_add"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/room/room_management_edit.html", context)


class administerroom_deleteView(View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        room = Room.objects.get(id=id)
        room.delete()
        return JsonResponse({"status": 'success'})


class open_dormitoryView(View):
    @staticmethod
    def get(request):
        open_days = Opening_booking.objects.all()
        open_days_page = paginate_list(request, open_days, 3)

        context = {
            "form": Opening_bookingForm(),
            "open_days": open_days_page}
        return render(request, "administer/dorm/open_dormitory.html", context)

    @staticmethod
    def post(request):
        form = Opening_bookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("open_dormitory"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/open_dormitory.html", context)


class open_dormitory_deleteView(View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        open_day = Opening_booking.objects.get(id=id)
        open_day.delete()
        return JsonResponse({"status": 'success'})


class open_dormitory_editView(View):
    @staticmethod
    def get(request, id):
        open_day = Opening_booking.objects.get(id=id)
        context = {
            "form": Opening_bookingForm(instance=open_day),
            "open_day": open_day
        }
        return render(request, "administer/dorm/open_dormitory_edit.html", context)

    @staticmethod
    def post(request, id):
        open_day = Opening_booking.objects.get(id=id)
        form = Opening_bookingForm(request.POST, instance=open_day)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("open_dormitory"))
        context = {
            "form": form
        }
        return render(request, "administer/dorm/open_dormitory_edit.html", context)


class booking_HomeView(View):
    @staticmethod
    def get(request):
        return render(request, "administer/booking/booking_home.html")

    @staticmethod
    def post(request):
        print("Yes")
        return HttpResponseRedirect(reverse("booking_home"))


class booking_View(View):
    @staticmethod
    def get(request):

        return render(request, "administer/booking/booking.html")


class booking_academic_year_View(View):
    @staticmethod
    def get(request):
        academic_years = Academic_year.objects.all().values('academic_year', 'id')
        context = {
            "academic_years": academic_years,
        }
        return render(request, "administer/booking/booking_academic_year.html", context)

    @staticmethod
    def post(request):
        academic_year = request.POST.get("academic_year")
        bookings = Booking.objects.filter(
            open_booking__academic_year=academic_year)
        context = {
            "bookings": bookings,

        }
        return render(request, "administer/booking/booking_academic_year.html", context)


class booking_dorm_View(View):
    @staticmethod
    def get(request):
        dorms = Dormitory.objects.all()

        context = {
            "dorms": dorms,
        }
        return render(request, "administer/booking/booking_dorm.html", context)

    @staticmethod
    def post(request):
        id_dorm = request.POST.get("dorm")
        try:
            bookings = Booking.objects.filter(
                room__floor__dorm_name__id=id_dorm)
        except:
            bookings = None

        if not bookings:
            messages.warning(request, "ไม่มีข้อมูลการจอง")
            return HttpResponseRedirect(reverse("booking_dorm"))
        context = {
            "bookings": bookings,
        }
        return render(request, "administer/booking/booking_dorm.html", context)


class booking_group_View(View):
    @staticmethod
    def get(request):
        groups = Group.objects.all()

        context = {
            "groups": groups,

        }
        return render(request, "administer/booking/booking_group.html", context)

    @staticmethod
    def post(request):
        bookings = []
        id_group = int(request.POST.get("group_id"))
        try:
            booking_all = Booking.objects.all()
            for booking in booking_all:
                if booking.get_user_group() == id_group:
                    bookings.append(booking)

        except:
            bookings = None

        if not bookings:
            messages.warning(request, "ไม่มีข้อมูลการจอง")
            return HttpResponseRedirect(reverse("booking_group"))
        context = {
            "bookings": bookings,
        }
        return render(request, "administer/booking/booking_group.html", context)


class confirmation_view(View):
    @staticmethod
    def get(request):
        confirmations = Booking_confirmation.objects.all()
        confirmations_page = paginate_list(request, confirmations, 3)

        context = {
            "confirmations": confirmations_page,
        }
        return render(request, "administer/booking/confirmation.html", context)


class booking_reportView(View):
    @staticmethod
    def get(request):
        return render(request, "administer/booking/booking_report.html")


class booking_reportDormView(View):
    @staticmethod
    def get(request):
        dorms = Dormitory.objects.all()
        context = {
            "dorms": dorms,
        }
        return render(request, "administer/booking/booking_report_dorm.html", context)

    @staticmethod
    def post(request):
        dorm = request.POST.get("dorm")
        # get is_room_available_floor
        dorm = Dormitory.objects.get(id=dorm)
        if not dorm:
            dorm = None
        try:
            room_available = dorm.is_room_available_floor()
            room_not_available = dorm.is_room_not_available_floor()
            all_room = room_available + room_not_available
            room_amount_total = dorm.get_room_amount_total()['amount__sum']
        except:
            room_available = None
            room_not_available = None
            all_room = None
            room_amount_total = None
            dorm = None
        context = {
            "dorm": dorm,
            "room_available": room_available,
            "room_not_available": room_not_available,
            "all_room": all_room,
            "room_amount_total": room_amount_total,
        }

        return render(request, "administer/booking/booking_report_dorm_dashboard.html", context)


class booking_reportGroupView(View):
    @staticmethod
    def get(request):
        groups = Group.objects.all()
        context = {
            "groups": groups,
        }

        return render(request, "administer/booking/booking_report_group.html", context)

    @staticmethod
    def post(request):
        group = request.POST.get("group")
        group = Group.objects.get(id=group)
        # เอากลุ่มออกมาและมีการเช็คกลุ่มเช็คกลุ่มที่มีการเช็คกลุ่มแล้ว

        return render(request, "administer/booking/booking_report_group_dashboard.html")
