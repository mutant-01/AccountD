from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    email_address = models.EmailField(unique=True, verbose_name="Email address")
    password = models.CharField(blank=True, max_length=2048)
    address = models.URLField(
        max_length=2048,
        verbose_name="Address in which this email can be used"
    )
    broken_count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Broken report count"
    )


class Account(models.Model):
    user_field = models.CharField(max_length=1024)
    password_field = models.TextField(blank=True)
    broken_count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Broken report count"
    )
    seen_count = models.BigIntegerField(default=0)
    address = models.URLField(
        max_length=2048,
        verbose_name="Address in which this account is usable"
    )
    email = models.ForeignKey(
        Email,
        models.SET_NULL,
        null=True,
    )
    owner = models.ForeignKey(User, models.CASCADE, null=True)
