from django.shortcuts import get_object_or_404, render, get_list_or_404
from . models import Blog
from django.contrib.auth.models import User

# Create your views here.


def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/list.html", {"blogs": blogs})


def detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/detail.html", {"blog": blog})

def create_blog(request, user):
    return render(request, "blog/create_blog.html", {"user": user})