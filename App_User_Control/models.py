from django.db import models
from django.contrib.auth.models import User as Auth_User


# Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=64)
#     password = models.CharField(max_length=64)
#     age = models.IntegerField()
#
#     genders=(
#         (1,'Male'),
#         (2,"Female"),
#         (3,'Anonymous')
#     )
#
#     levels=(
#         ('L1','Advanced User'),
#         ('L2', 'Standard User'),
#         ('L3', 'Beginner User')
#     )
#
#     gender=models.PositiveSmallIntegerField(choices=genders)
#     level=models.CharField(max_length=2,choices=levels)
#     email=models.EmailField(max_length=128)
#     address=models.CharField(max_length=128, null=True)
#     portrait=models.ImageField(null=True)
#     update_time=models.DateTimeField()
#
#
#     class Meta:
#         app_label = "App_User_Control"
#         verbose_name="User"
#         verbose_name_plural='Users'
#
#     def __str__(self):
#         return self.username
#
# class Patients(models.Model):
#     username=models.CharField(max_length=64)
#     age = models.IntegerField()
#     genders=(
#         (1,'Male'),
#         (2,"Female"),
#         (3,'Intersex')
#     )
#     gender = models.PositiveSmallIntegerField(choices=genders)
#     occupation=models.CharField(max_length=64)
#     disease=models.CharField(max_length=128)
#     description=models.CharField(max_length=1024)
#     update_time=models.DateTimeField()
#
#     class Meta:
#         app_label="App_User_Control"
#         verbose_name="Patient"
#         verbose_name_plural='Patients'
#
#     def __str__(self):
#         return self.username
#
class Patient(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    genders = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Unknown')
    )
    gender = models.PositiveSmallIntegerField(choices=genders)
    description = models.CharField(max_length=1024)
    device=models.CharField(max_length=1024,null=True ,help_text="Max length is 1024, multiple devices split by comma.")

    class Meta:
        app_label = "App_User_Control"

    def __str__(self):
        return self.name


class SearchHistory(models.Model):
    user = models.ForeignKey(Auth_User, null=True, blank=True, on_delete=models.SET_NULL)
    search_text = models.CharField(max_length=128)
    search_time = models.DateTimeField()

    class Meta:
        app_label = "App_User_Control"

    def __str__(self):
        return str(self.user)+" ("+str(self.user.username)+")"

class UserPatient(models.Model):
    user = models.ForeignKey(Auth_User, null=True, blank=True, on_delete=models.SET_NULL)
    patient=models.ForeignKey(Patient,null=True,blank=True,on_delete=models.SET_NULL)

    class Meta:
        app_label = "App_User_Control"

    def __str__(self):
        return str(self.user)+" ("+str(self.user.username)+")"