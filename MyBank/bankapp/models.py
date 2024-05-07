from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be 10 digits')],
        unique=True,
        blank=False,
        null=False
    )
    user_id = models.AutoField(primary_key=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aadhar_number = models.CharField(
        max_length=12,
        validators=[RegexValidator(regex=r'^\d{12}$', message='Aadhar number must be 12 digits')],
        unique=True,
        blank=False,
        null=False       
    )


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ACCOUNT_CHOICES = (
        ('SAVING', 'SAVING'),
        ('CURRENT', 'CURRENT')
    )
    account_type = models.CharField(choices=ACCOUNT_CHOICES, max_length=20)
    account_number = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
