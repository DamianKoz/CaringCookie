from django.urls import path
from . import views
from profiles.views import ChangePasswordView
urlpatterns = [
    path("register", views.register_request, name="register"),
    path("profile", views.profile, name="users-profile"),
    path("changeProfile/<int:pk>", views.changeProfile, name="change-profile"),
    path('password-change/', ChangePasswordView.as_view(), name="password-change")
]