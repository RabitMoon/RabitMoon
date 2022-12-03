from django.contrib import admin
from course.models import course,dataStructure,DBMS,digitalElectronics,Maths,Oop

# Register your models here.

admin.site.register([course,dataStructure,DBMS,digitalElectronics,Maths,Oop])