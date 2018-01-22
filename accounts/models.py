from django.db import models


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
