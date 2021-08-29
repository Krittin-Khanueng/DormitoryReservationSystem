from django.shortcuts import render

from .forms import DormitoryForm
from dorm.models import Dormitory

from django.views import View
from django.contrib import messages


class administerView(View):
    def get(self, request):
        return render(request, "administer/base_admin_page.html")


class administerdashboardView(View):
    def get(self, request):
        return render(request, "administer/dashboard.html")


class administerdormView(View):
    def get(self, request):

        context = {
            "form": DormitoryForm(),
            "dorms": Dormitory.objects.all()
        }
        return render(request, "administer/dorm_management.html", context)

    def post(self, request):
        form = DormitoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกสำเร็จ")
            return render(request, "administer/dorm_management.html")
        else:
            context = {
                "form": form
            }
            return render(request, "administer/dorm_management.html", context)
