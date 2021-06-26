from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from endpoint.forms import UserCreateForm, UserLoginForm
from django.views.decorators.csrf import csrf_exempt
from endpoint.models import User


def _home(request):
    return render(request, "endpoint/home.html")


@csrf_exempt
def _register(request):
    form = UserCreateForm()

    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            avatar = form.cleaned_data.get("avatar")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            user = User(
                first_name=first_name, last_name=last_name, email=email,
                phone=phone, avatar=avatar, password1=password1, password2=password2
            )
            user.save()

            return HttpResponse("You have successfully registered a user!")

        return HttpResponse(f"{form.error_messages}")

    # return render(request, "endpoint/register.html", {"form": form})
    return HttpResponse("Register Now...")


@csrf_exempt
def _login(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request, email=email, password=password
            )
            if user is not None:
                login(request, user)
                return HttpResponse(f"{email}: you have successfully logged in!")
        return HttpResponse(f"{form.error_messages}")

    return HttpResponse("Login Now...")


@csrf_exempt
def _logout(request):
    logout(request)
    return HttpResponse("You have successfully logged out!")
