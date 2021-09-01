from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/', views.administerView.as_view()),
    path('dashboard/', views.administerdashboardView.as_view(), name='dashboard'),
    path('dorm/', views.administerdormView.as_view(), name='management_dorm'),
    path('dorm/add/', views.administerdorm_addView.as_view(),
         name='management_dorm_add'),
    path('dorm/edit/<int:id>/', views.administerdorm_editView.as_view(),
         name='management_dorm_edit'),
    path('dorm/delete/', views.administerdorm_deleteView.as_view(),
         name="management_dorm_delete"),

    path('dorm/floor/add/', views.administerfloor_addView.as_view(),
         name="management_floor_add"),
    path("dorm/room/add/", views.administerroom_addView.as_view(),
         name="management_room_add"),
    path("dorm/room/edit/<int:id>/", views.administerroom_editView.as_view(),
         name="management_room_edit"),
    path("dorm/room/delete/", views.administerroom_deleteView.as_view(),
         name="management_room_delete"),
    path('dorm/open/dormitory/',
         views.open_dormitoryView.as_view(), name="open_dormitory"),
    path('dorm/open/dormitory/edit/<int:id>/',
         views.open_dormitory_editView.as_view(), name="open_dormitory_edit"),
    path('dorm/open/dormitory/delete/',
         views.open_dormitory_deleteView.as_view(), name="open_dormitory_delete"),
    path('booking/', views.booking_HomeView.as_view(), name="booking_home"),
    path('booking/view/', views.booking_View.as_view(), name="booking_view"),
    path('booking/view/academic-year/',
         views.booking_academic_year_View.as_view(), name="booking_academic_year"),
    path('booking/view/dorm/', views.booking_dorm_View.as_view(), name="booking_dorm"),
    path('confirmation/view/', views.confirmation_view.as_view(),
         name="confirmation_view"),
    path('booking/report/', views.booking_reportView.as_view(),
         name="booking_report"),
    path('booking/report/dorm/', views.booking_reportDormView.as_view(),
         name="booking_report_dorm"),
    path('booking/report/group/', views.booking_reportGroupView.as_view(),
         name="booking_report_group"),


]
