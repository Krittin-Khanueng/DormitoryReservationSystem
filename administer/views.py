from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from booking.models import Opening_booking
from dorm.models import Dormitory, Room
from .forms import DormitoryForm, FloorForm, RoomForm, Opening_bookingForm


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
        paginator = Paginator(dorms, 3)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            dormPage = paginator.page(page)
        except (EmptyPage, InvalidPage):
            dormPage = paginator.page(paginator.num_pages)

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
        else:
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
        else:
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
        else:
            context = {
                "form": form
            }
            return render(request, "administer/dorm/floor/floor_management_add.html", context)


class administerroom_addView(View):
    @staticmethod
    def get(request):
        rooms = Room.objects.all()
        paginator = Paginator(rooms, 3)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            roomPage = paginator.page(page)
        except (EmptyPage, InvalidPage):
            roomPage = paginator.page(paginator.num_pages)

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
        else:
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
        else:
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
        paginator = Paginator(open_days, 3)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            open_daysPage = paginator.page(page)
        except (EmptyPage, InvalidPage):
            open_daysPage = paginator.page(paginator.num_pages)

        context = {
            "form": Opening_bookingForm(),
            "open_days": open_daysPage}
        return render(request, "administer/dorm/open_dormitory.html", context)

    @staticmethod
    def post(request):
        form = Opening_bookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return HttpResponseRedirect(reverse("open_dormitory"))
        else:
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
        print("Hello world")
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
        else:
            context = {
                "form": form
            }
            return render(request, "administer/dorm/open_dormitory_edit.html", context)
