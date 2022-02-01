from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.shortcuts import redirect
from . models import Blog
from django.contrib.auth.models import User

from .forms import CreateBlogForm, ChangeBlogForm

# Create your views here.


def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/list.html", {"blogs": blogs})

def detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/detail.html", {"blog": blog})

def create_blog(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateBlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid() and request.user.is_authenticated:
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            type = form.cleaned_data['type']
            newentry = Blog(title=title, content=content, author = request.user, type = type)
            newentry.save()
            return redirect("blog_list")
    else:
        form = CreateBlogForm()

    return render(request, "blog/create_blog.html", {'form': form})


def change_blog(request,pk):
    
    entrytochange = get_object_or_404(Blog, pk=pk)
    initial_data={
            'title':entrytochange.title,
            'content':entrytochange.content,
    }
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChangeBlogForm(request.POST)
        # check whether it's valid:
        
        if form.is_valid() and request.user.is_authenticated and request.user == entrytochange.author:
            entrytochange.title = form.cleaned_data['title']
            entrytochange.content = form.cleaned_data['content']
            entrytochange.save()
            return redirect("blogs_detail", pk)
    else:
        form = ChangeBlogForm(initial=initial_data)
    return render(request, "blog/change_blog.html", {'form': form, 'entrytochange': entrytochange})