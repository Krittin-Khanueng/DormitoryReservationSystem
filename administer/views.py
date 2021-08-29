from django.shortcuts import render

from .forms import DormitoryForm
from dorm.models import Dormitory

from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage


class administerView(View):
    def get(self, request):
        return render(request, "administer/base_admin_page.html")


class administerdashboardView(View):
    def get(self, request):
        return render(request, "administer/dashboard.html")


class administerdormView(View):
    def get(self, request):
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
