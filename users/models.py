from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from django.core.exceptions import ValidationError
# Create your models here.

def validate_phone(value):
    pattern = r'+996'
    if not re.match(pattern, value):
        raise ValidationError('Номер телефона должен быть в формате +996 .')
    
class Users(AbstractUser):
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=13, unique=True, validators=[validate_phone])
    age = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username