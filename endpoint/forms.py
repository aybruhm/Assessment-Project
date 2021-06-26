from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from endpoint.models import User


class UserCreateForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "phone",
            "email", "avatar"
        ]

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'phone': forms.TextInput(),
            'email': forms.EmailInput(),
        }


class UserLoginForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    email = forms.CharField(
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )