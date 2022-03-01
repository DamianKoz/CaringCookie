from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.shortcuts import redirect
from . models import Blog, Images, Category
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator

from .forms import CreateBlogForm, CreateBlogFormExtended, SendMailForm

# Create your views here.


def list_blogs(request):
    blogs = Blog.objects.all()
    categorys = Category.objects.all()
    blog_paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page = blog_paginator.get_page(page_number)
    
    context = {
        'categorys' : categorys,
        'page' : page
    }
    return render(request, "blog/list.html", context)

def detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    images = Images.objects.filter(blog=blog)
    return render(request, "blog/detail.html", {"blog": blog, "images": images})

def create_blog(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateBlogFormExtended(request.POST, request.FILES or None)
        files = request.FILES.getlist('images')
        # check whether it's valid:
        if form.is_valid() and request.user.is_authenticated:
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            type = form.cleaned_data['type']
            producttype = form.cleaned_data['producttype']
            category = form.cleaned_data['category']
            newentry = Blog(title=title, content=content, author = request.user, type = type, producttype = producttype, category = category)
            newentry.save()
            for f in files:
                Images.objects.create(blog=newentry,image=f)
            return redirect("blogs_detail", newentry.pk)
    else:
        form = CreateBlogFormExtended()

    return render(request, "blog/create_blog.html", {'form': form})


def change_blog(request,pk):
    
    entrytochange = get_object_or_404(Blog, pk=pk)
    initial_data={
            'title':entrytochange.title,
            'content':entrytochange.content,
            'type':entrytochange.type,
            'producttype':entrytochange.producttype,
            'category':entrytochange.category
    }
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateBlogFormExtended(request.POST, request.FILES or None)
        files = request.FILES.getlist('images')
        # check whether it's valid:
        
        if form.is_valid() and request.user.is_authenticated and request.user == entrytochange.author:
            entrytochange.title = form.cleaned_data['title']
            entrytochange.content = form.cleaned_data['content']
            entrytochange.type = form.cleaned_data['type']
            entrytochange.producttype = form.cleaned_data['producttype']
            entrytochange.category = form.cleaned_data['category']
            entrytochange.save()
            if files:
                deleteOldPictures(entrytochange.pk)
                for f in files:
                    Images.objects.create(blog=entrytochange,image=f)
            return redirect("blogs_detail", pk)
    else:
        form = CreateBlogFormExtended(initial=initial_data)
    return render(request, "blog/change_blog.html", {'form': form, 'entrytochange': entrytochange})


def delete_blog(request,pk):
    
    entrytodelete = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
                
        if  request.user.is_authenticated and request.user == entrytodelete.author:
            entrytodelete.delete()
            return redirect("successfully_deleted_blog")
            
    return render(request, "blog/delete_blog.html", {'entrytodelete': entrytodelete})


def successfully_deleted_blog(request):
     
    return render(request, "blog/successfully_deleted_blog.html")  

def my_blogs(request):
    if request.user.is_authenticated:
        my_blogs = Blog.objects.filter(author=request.user)
        blog_paginator = Paginator(my_blogs, 10)
        page_number = request.GET.get('page')
        page = blog_paginator.get_page(page_number)
        
        context = {
            'categorys' : Category.objects.all(),
            'page' : page
        }

        return render(request, "blog/list.html", context)
    raise Http404("Du hast entweder keine Beiträge erstellt oder du bist nicht eingeloggt.")

def deleteOldPictures(pk):
    Images.objects.filter(blog=pk).delete()
    
def category(request, name):
    requestedcategory= get_object_or_404(Category, name=name)
    blogsofcategory = Blog.objects.filter(category=requestedcategory)
    blog_paginator = Paginator(blogsofcategory, 10)
    page_number = request.GET.get('page')
    page = blog_paginator.get_page(page_number)
            
    context = {
        'categorys' : Category.objects.all(),
        'requestedcategory': requestedcategory,
        'page' : page
    }

    return render(request, "blog/list.html", context)  

def search(request):
    results = []
    if request.method == "GET":

        query = request.GET.get('search')

    if query == '':

        query = 'None'

    results = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    return render(request, 'blog/search.html', {'query': query, 'results': results})
    
def faqs(request):
    
    if request.method == 'POST':
            
        form = SendMailForm()

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_mail = form.cleaned_data['mail']

            send_mail(
            subject,
            message,
            from_mail,
            ['cookiecaring@gmail.com'],
            fail_silently=False,
            )
    else:
        form = SendMailForm()

    return render(request, "blog/faqs.html", {'form': form} )
