from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

class Projects(models.Model):
    sitename=models.CharField(max_length=30)
    image=CloudinaryField('image', null=True)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    url=models.URLField(max_length=60)
    location = models.CharField(max_length=60, blank=True)
    date=models.DateField(auto_now=True)
    screen1=CloudinaryField('image', null=True)
    screen2=CloudinaryField('image', null=True)

    class Meta:
        ordering=['-sitename']

    def __str__(self):
        self.sitename
    @classmethod
    def search_project(cls,word):
        searched=cls.objects.filter(sitename__icontains=word)
        return searched

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=CloudinaryField('image', null=True)
    bio=models.CharField(max_length=60)
    class Meta:
        ordering=['-profile']

class Comments(models.Model):
    pro_id=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)

class Rates(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    


