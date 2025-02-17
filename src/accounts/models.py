from django.db import models
from django.contrib.auth.models import AbstractUser

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255)
    profession = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def str(self):
        return self.username
