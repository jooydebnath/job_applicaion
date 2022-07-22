from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Skils(models.Model):
    skils = models.CharField(max_length=50)

    def __str__(self):
        return self.skils

class GeneralCategory(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    skils = models.ForeignKey(Skils, on_delete=models.CASCADE)
    phone = PhoneNumberField(max_length=14)
    agree = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

class SpecialSkilledCategory(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    skils = models.ForeignKey(Skils, on_delete=models.CASCADE)
    phone = PhoneNumberField(max_length=14)
    agree = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

class AutismCategory(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    skils = models.ForeignKey(Skils, on_delete=models.CASCADE)
    phone = PhoneNumberField(max_length=14)
    autism_id = models.CharField(max_length=20)
    agree = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

class JobApply(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Salary = models.CharField(max_length=8)
    resume = models.FileField(upload_to='documents/')
    accept_all = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)