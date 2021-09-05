from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("context/", views.ContextPageView.as_view(), name="context"),
    path('psupassport/callback/', views.CallBackView.as_view(), name='callback'),
]
