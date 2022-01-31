from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_blogs, name="blog_list"),
    path("blog/<int:pk>", views.detail_view, name="blogs_detail"),
    path("create_blog", views.create_blog, name="create_blog"),
    path("change_blog/<int:pk>", views.change_blog, name="change_blog")
]
