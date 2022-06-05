from django.db import models

from helpers.models import TrackingModel
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import jwt
from django.conf import settings
from datetime import datetime, timedelta

# Create your models here.


def upload_to(instance, filename):
    return 'people/{filename}'.format(filename=filename)


class MyUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):

    PEOPLE = 'P'
    COMPANY = 'C'
    TYPEOFUSER = [
        (PEOPLE, _('People')),
        (COMPANY, _('Company')),
    ]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    email_verified = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this users email is verified. "

        ),
    )
    parent_id = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(
        _("Image"), upload_to=upload_to,  default='people/noimage.jpg')
    cargo = models.CharField(_("cargo"), max_length=150, blank=True)
    typeofuser = models.CharField(
        max_length=8,
        choices=TYPEOFUSER,
        default=PEOPLE,
    )

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def token(self):
        token = jwt.encode({'username': self.username,
                            'email': self.email,
                            'exp': datetime.utcnow() + timedelta(hours=24)},
                           settings.SECRET_KEY, algorithm='HS256')
        return token
