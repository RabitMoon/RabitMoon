from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class blog(models.Model):
    sno = models.AutoField(primary_key=True)
    Auth = models.CharField(max_length=255)
    title = models.CharField(max_length=225)
    about = models.TextField(max_length=200)
    # email = models.CharField(max_length=40)
    time =models.DateTimeField(auto_now=True,blank=True)
    Content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=130)


    def __str__(self) -> str:
        return 'data of ' + self.title +' - '+ self.Auth