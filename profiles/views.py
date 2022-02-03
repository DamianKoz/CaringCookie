from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from .forms import NewUserForm, NewProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

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

@login_required
def createProfile(request):
    return render(render, 'profiles/createProfile.html')


@login_required
def changeProfile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    user_form = UpdateUserForm()
    profile_form = UpdateProfileForm()
    return render(request, 'profiles/changeProfile.html', context={'user_form': user_form, 'profile_form': profile_form})


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

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'profiles/changePassword.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')