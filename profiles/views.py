from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("main:homepage")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
# return render(request=request, template_name="main/login.html", context={"login_form":form})
    return render(request, "profiles/login.html", context={"login_form":form})

@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

@csrf_exempt
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.info(request, "Registration successful." )
			return redirect("blog_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, "profiles/register.html", context={"register_form":form})