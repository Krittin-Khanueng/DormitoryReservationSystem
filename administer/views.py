from django.conf import settings
import administer
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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView


class loginView(LoginView):
    template_name = 'administer/login.html'
    redirect_field_name = 'next'
    redirect_authenticated_user = True


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/manage/login'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


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


class administerView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/base_admin_page.html")


class administerdashboardView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/dashboard.html")


class administerdorm_addView(AdminStaffRequiredMixin, View):
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


class administerdorm_editView(AdminStaffRequiredMixin, View):
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


class administerdorm_deleteView(AdminStaffRequiredMixin, View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        dorm = Dormitory.objects.get(id=id)
        dorm.delete()
        return JsonResponse({"status": 'success'})


class administerdormView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/dorm/dorm_management.html")


class administerfloor_addView(AdminStaffRequiredMixin, View):
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


class administerroom_addView(AdminStaffRequiredMixin, View):
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


class administerroom_editView(AdminStaffRequiredMixin, View):
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


class administerroom_deleteView(AdminStaffRequiredMixin, View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        room = Room.objects.get(id=id)
        room.delete()
        return JsonResponse({"status": 'success'})


class open_dormitoryView(AdminStaffRequiredMixin, View):
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


class open_dormitory_deleteView(AdminStaffRequiredMixin, View):
    @staticmethod
    def post(request):
        id = request.POST.get("id")
        open_day = Opening_booking.objects.get(id=id)
        open_day.delete()
        return JsonResponse({"status": 'success'})


class open_dormitory_editView(AdminStaffRequiredMixin, View):
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


class booking_HomeView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/booking/booking_home.html")


class booking_View(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/booking/booking.html")


class booking_academic_year_View(AdminStaffRequiredMixin, View):
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


class booking_dorm_View(AdminStaffRequiredMixin, View):
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


class booking_group_View(AdminStaffRequiredMixin, View):
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


class confirmation_view(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        confirmations = Booking_confirmation.objects.all()
        confirmations_page = paginate_list(request, confirmations, 3)

        context = {
            "confirmations": confirmations_page,
        }
        return render(request, "administer/booking/confirmation.html", context)


class booking_reportView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "administer/booking/booking_report.html")


class booking_reportDormView(AdminStaffRequiredMixin, View):
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
            booikng_count = Booking.objects.filter(
                room__floor__dorm_name=dorm).count()
            booking_confirmation = Booking_confirmation.objects.filter(
                booking__room__floor__dorm_name=dorm, is_confirmed=True).count()
            booking_not_confirm = Booking_confirmation.objects.filter(
                booking__room__floor__dorm_name=dorm, is_confirmed=False).count()
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
            "booikng_count": booikng_count,
            "booking_confirmation": booking_confirmation,
            "booking_not_confirm": booking_not_confirm,
        }
        return render(request, "administer/booking/booking_report_dorm_dashboard.html", context)


class usersView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        users = User.objects.all()
        users_page = paginate_list(request, users, 3)

        context = {
            "users": users_page,
        }
        return render(request, "administer/users/users.html", context)


class user_groupsView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        groups = Group.objects.all()
        context = {
            "groups": groups,
        }
        return render(request, "administer/users/user_groups.html", context)

    @staticmethod
    def post(request):
        group_id = request.POST.get("group_id")
        try:
            users = User.objects.filter(groups__id=group_id)
            users = paginate_list(request, users, 10)
        except:
            users = None
        if not users:
            messages.warning(request, "ไม่มีข้อมูลการจอง")
            return HttpResponseRedirect(reverse("user_groups"))
        context = {
            "users": users,
        }
        return render(request, "administer/users/user_groups_list.html", context)


class user_detailView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request, user_id):
        account = User.objects.get(id=user_id)
        context = {
            "account": account,
        }
        return render(request, "administer/users/user_detail.html", context)


class user_deleteView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, "ลบข้อมูลสำเร็จ")
        return HttpResponseRedirect(reverse("users"))


class user_manageView(AdminStaffRequiredMixin, View):
    @staticmethod
    def get(request):
        groups = Group.objects.all()

        context = {
            "groups": groups,
        }
        return render(request, "administer/users/user_manage.html", context)

    def post(self, request):
        try:
            users = User.objects.filter(
                groups__id=request.POST.get("group_id"))
        except Exception as e:
            users = None
        if not users:
            messages.warning(request, "ไม่มีข้อมูลการจอง")
            return HttpResponseRedirect(reverse("user_manage"))
        for user in users:
            user.account.current_state = 'มีสิทธิ์จอง'
        user.account.save()
        messages.success(request, "จัดการสิทธิ์สำเร็จ")
        return HttpResponseRedirect(reverse("user_manage"))
