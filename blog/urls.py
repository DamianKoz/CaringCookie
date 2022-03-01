from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_blogs, name="blog_list"),
    path("blog/<int:pk>", views.detail_view, name="blogs_detail"),
    path("create_blog", views.create_blog, name="create_blog"),
    path("change_blog/<int:pk>", views.change_blog, name="change_blog"),
    path("delete_blog/<int:pk>", views.delete_blog, name="delete_blog"),
    path("delete_blog/successfully_deleted_blog", views.successfully_deleted_blog, name="successfully_deleted_blog"),
    path("my_blogs", views.my_blogs, name="my_blogs"),
    path("categories/<str:name>", views.category, name="category"),
    path("search", views.search, name="search"),
    path("faqs", views.faqs, name="faqs")
]
