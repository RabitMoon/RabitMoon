from django.contrib import admin
from django.urls import path,include
from course import views

urlpatterns=[
    path('', views.courseHome, name='home'),

    path('dataStructure/',views.dataStructureHome,name='subTitle'),
    path('dataStructure/<str:slug>',views.dataStructureContent,name='subTitle'),
    
    path('Oop/',views.OopHome,name='Oop'),
    path('Oop/<str:slug>',views.OopContent,name='OopPage'),
    
    path('DBMS/',views.DBMSHome,name='Dbms'),
    path('DBMS/<str:slug>',views.DBMSContent,name='DbmsPage'),
    
    path('digitalElectronics/',views.DEHome,name='subTitle'),
    path('digitalElectronics/<str:slug>',views.DEContent,name='subTitle'),
    
    path('Maths/',views.MathsHome,name='subTitle'),
    path('Maths/<str:slug>',views.MathsContent,name='subTitle'),
    
    # path('<str:slug>',views.subPost,name='subPost'),
]