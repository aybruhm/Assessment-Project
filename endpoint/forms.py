from django import forms
from endpoint.models import User


class UserCreateForm(forms.ModelForm):
    """
    A form that inherits from ModelForm,
    and creates a user, with privileges, from the given
    email and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }

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

    def clean_password2(self):
        """
        Check that the two password entries match
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """
        Save the provided password in hashed format
        """
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with privileges, from the given 
    email and password.
    """

    email = forms.CharField(
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    error_messages = {
        'invalid_login':
            f"Please enter a correct {email} and password. Note that both "
            "fields may be case-sensitive.",
        'inactive': "This account is inactive.",
    }
