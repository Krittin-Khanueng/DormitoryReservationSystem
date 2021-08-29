from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class administerView(TemplateView):
    template_name = "administer/base_admin_page.html"


class administerdashboardView(TemplateView):
    template_name = "administer/admin_dashboard.html"


class administerdormView(TemplateView):
    template_name = "administer/admin_dorm_management.html"
