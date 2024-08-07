from django.contrib import admin
from django.urls import path, include
from page import views


urlpatterns = [
    path("", views.home_view, name="home_view_name"),
]
