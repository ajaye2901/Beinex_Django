from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class Role(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    )
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)

class User(AbstractUser):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    )
    mobile_number_errors = {
        "required": "Mobile number is required",
        "invalid": "Enter a valid 10 digit mobile number"
        + "without spaces, + or isd code.",
    }
    _mobile_regex_validator = RegexValidator(
        regex=r"^\d{10}$", message="Phone number must be 10 digits without + or spaces."
    )
    email_errors = {
        "required": "Email number is required",
        "invalid": "Enter a valid Email" + "without spaces",
    }
    _email_regex_validator = RegexValidator(
        regex=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",
        message="Email must be Valid",
    )

    user_id = models.AutoField(primary_key=True)
    email = models.CharField(
        "Email",
        max_length=50,
        validators=[_email_regex_validator],
        blank=False,
        null=False,
        unique=True,
        error_messages=email_errors,
    )
    mobile_phone = models.CharField(
        "Mobile Number",
        max_length=10,
        validators=[_mobile_regex_validator],
        blank=False,
        null=False,
        unique=True,
        error_messages=mobile_number_errors,
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    role_id = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.username


class Snippet(models.Model) :
    snippet_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)
