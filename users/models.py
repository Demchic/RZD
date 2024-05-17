from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=30, blank=True, null=True,)
    tab_number = models.CharField('Табельный номер', max_length=7, blank=True, null=True,)
    phone_number = models.CharField('Рабочий телефон', max_length=12, blank=True, null=True, )
