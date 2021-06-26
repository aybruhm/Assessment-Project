from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is 
    unique identifiers for authentication instead of username
    """

    def create_user(self, first_name, last_name, phone, email, password, **other_fields):
        if not email:
            raise ValueError(_("The Email must be set"))

        if not phone:
            raise ValueError(_("The Phone number must be set"))

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name, last_name=last_name,
            phone=phone, email=email, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone, email, password, **other_fields):
        """
        Create and save Superuser with the given email and password
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(first_name, last_name, phone, email, password, **other_fields)
