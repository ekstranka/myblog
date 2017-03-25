from django.db import models
from django.utils import timezone


class Service(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    subtitle=models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class Dotaz(models.Model):
    dotaz_id = models.AutoField(primary_key=True)
    sluzba = models.CharField(max_length=200)
    jmeno = models.CharField(max_length=25)
    prijmeni=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    mobil=models.CharField(max_length=13)
    zprava = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    odpovezeno = models.BooleanField(default=False)

    def __str__(self):
        return self.zprava


    
