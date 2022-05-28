from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('details/<int:pk>/', views.eventdetails.as_view(), name='details'),


]