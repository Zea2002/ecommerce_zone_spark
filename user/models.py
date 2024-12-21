# Description: This file contains the models for the user app.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.files.storage import default_storage


# Create your models here.

# Custom User model that extends the AbstractUser model
class User(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username #return username


# Profile model that extends the User model
class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message="Phone number must be exactly 11 digits."
            )
        ]
    )
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username #return username

    def clean(self): #clean method to validate the phone number
        super().clean()
        if self.phone and len(self.phone) != 11:
            raise ValidationError({'phone': "Phone number must be exactly 11 digits."})

    def save(self, *args, **kwargs): #save method to delete the old profile picture if a new one is uploaded                
        # Delete the old profile picture if a new one is uploaded   
        if self.pk:
            old_profile = Profile.objects.filter(pk=self.pk).first()
            if old_profile and old_profile.profile_pic and self.profile_pic != old_profile.profile_pic:
                default_storage.delete(old_profile.profile_pic.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs): 
        # Delete the profile picture when the profile is deleted
        if self.profile_pic:
            default_storage.delete(self.profile_pic.path)
        super().delete(*args, **kwargs)
