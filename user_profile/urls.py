
from django.urls import path, include
from user_profile.views import login_view, logout_view, register_view

app_name = "user_profile"
urlpatterns = [
    path("login/", login_view, name="login_view_name"),
    path("logout/", logout_view, name="logout_view_name"),
    path("register/", register_view, name="register_view_name"),

]
