from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home/home.html')

# def course(request):
#     return render(request,'home/course.html')

