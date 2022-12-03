from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class course(models.Model):
    Auth = models.CharField(max_length=255)
    subject = models.CharField(max_length=225)
    # subject = models.CharField(max_length=200)
    # title = models.CharField(max_length=225)
    time =models.DateTimeField(auto_now=True,blank=True)
    # Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)


    def __str__(self) -> str:
        return 'data of ' + self.subject

class dataStructure(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)
    time =models.DateTimeField(auto_now=True,blank=True)

    def __str__(self) -> str:
        return 'data of ' + self.title

class Oop(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)
    time =models.DateTimeField(auto_now=True,blank=True)

    def __str__(self) -> str:
        return 'data of ' + self.title

class DBMS(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)
    time =models.DateTimeField(auto_now=True,blank=True)

    def __str__(self) -> str:
        return 'data of ' + self.title

class digitalElectronics(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)
    time =models.DateTimeField(auto_now=True,blank=True)

    def __str__(self) -> str:
        return 'data of ' + self.title

class Maths(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)
    time =models.DateTimeField(auto_now=True,blank=True)

    def __str__(self) -> str:
        return 'data of ' + self.title

