from django.urls import path
from . import views

urlpatterns = [
	path("", views.HomePageView.as_view(), name="index" ),
	path('psupassport/callback/', views.CallBackView.as_view(), name='callback'),
]
