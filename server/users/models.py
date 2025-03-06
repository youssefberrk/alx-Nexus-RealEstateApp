from django.db import models
from django.contrib.auth.models import AbstractUser

class TenantManager(models.TextChoices):
    TENANT = 'TENANT', 'Tenant' # 0 for db and 1 for display
    MANAGER = 'MANAGER', 'Manager'


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=TenantManager.choices, default=TenantManager.TENANT)
    phone_number = models.CharField(max_length=20)
    