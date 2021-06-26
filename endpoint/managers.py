from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is 
    unique identifiers for authentication instead of usernames
    """
    def create_user(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Create and save Superuser with the given email and password
        """
        user = self.create_user(email=email, password=password)
        user.save(using=self._db)
        return user 