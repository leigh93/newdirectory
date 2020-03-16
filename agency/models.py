from django.db import models

# CLOUDINARY IMPORTS
# from cloudinary.models import CloudinaryField
from pyuploadcare.dj.models import ImageField


# Create your models here.

class Agency(models.Model):
    agencyname = models.CharField(max_length = 200)
    registration_no = models.IntegerField()
    agency_logo = ImageField(blank=True,manual_crop="")
    agency_image = ImageField(blank=True,manual_crop="")
    
    def __str__(self):
        return self.agencyname

    class Meta:
        ordering = ['agencyname']
        verbose_name_plural = 'agencies'

    @classmethod
    def search_by_name(cls,search_term):
        agency = cls.objects.filter(agenncyname__icontains=search_term)
        return agency

class Agent(models.Model):
    name = models.CharField(max_length = 100)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE,blank =True)
    registration_no = models.IntegerField()
    email = models.EmailField()
    phone_no = models.IntegerField()
    profile_image = ImageField(blank=True,manual_crop="")


# class Property(models.Model):
#     avatar = CloudinaryField('avatar')
#     property_type = [

#     ]

