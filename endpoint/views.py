from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from endpoint.forms import UserCreateForm, UserLoginForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def _register(request):
    form = UserCreateForm()

    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()
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
