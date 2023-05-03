from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):

    name = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(
        ('Mobile Number'), max_length=14, null=True, blank=True)
    email = models.EmailField(
        _("Email address"), null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('D', 'Not Given'),
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True, default="D")
    birthdate = models.DateField(blank=True, null=True)

# Client Table


class Clienttable(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# Work Table


class workTable(models.Model):
    link = models.CharField(max_length=100, null=True, blank=True)
    WORK_CHOICES = (
        ('Y', 'Youtube'),
        ('I', 'Instagram'),
        ('O', 'Other'),
    )
    workType = models.CharField(
        max_length=10, choices=WORK_CHOICES, null=True)

    def __str__(self):
        strname = ""
        for i in range(3):
            if(self.WORK_CHOICES[i][0] == self.workType):
                strname = self.WORK_CHOICES[i][1]

        return "workTable object (" + str(self.id) + ") " + strname

# Artist Table


class artistTable(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    work = models.ManyToManyField(workTable)

    def __str__(self):
        return self.name + " (" + str(id)+")"


# Post signal to create object for client table on new user register
@receiver(post_save, sender=CustomUser)
def task_handler(sender, instance, **kwargs):

    Clienttable.objects.create(user=instance, name=instance.name)
