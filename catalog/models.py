from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class BloodGroup(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    hospid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    Apositive = models.IntegerField(null=True)
    Anegative = models.IntegerField(null=True)
    Bpositive = models.IntegerField(null=True)
    Bnegative = models.IntegerField(null=True)
    ABpositive = models.IntegerField(null=True)
    ABnegative = models.IntegerField(null=True)
    Opositive = models.IntegerField(null=True)
    Onegative = models.IntegerField(null=True)

    def __str__(self):
        return self.name
        return self.email 
        return self.contact
        return self.location
        


class Donor(models.Model):
    STATUS = (
        ('Available' , 'Available'),
        ('Unavailable' , 'Unavailable'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    donorid = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    bloodgroup = models.ForeignKey(BloodGroup, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    
    def __str__(self):
        return self.name
        return self.email
        return self.contact
        return self.location
        return self.bloodgroup




    

