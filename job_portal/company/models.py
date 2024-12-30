from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$', message={"Contact number is not in valid format."})

class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=15, validators=[phone_regex])

    def __str__(self):
        return self.name
