from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("profile", views.profile, name="users-profile"),
  
]


