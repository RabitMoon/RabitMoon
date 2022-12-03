from django.shortcuts import render,HttpResponse
from course.models import course,dataStructure,Oop,digitalElectronics,DBMS,Maths
# Create your views here.

def courseHome(request):
    allPost = course.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/course.html',context)

def subPost(request,slug):
    allPost = course.objects.all()
    context = {'allPost':allPost}
    
    post = course.objects.filter(slug=slug).first()
    # chapter = course.objects.filter(tiitle=title).first()
    
    context = {'course':post,'allPost':allPost}
    return render(request,'course/chapter.html',context)

def dataStructureHome(request):
    allPost = dataStructure.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/chapter.html',context)


def dataStructureContent(request,slug):
    allPost = dataStructure.objects.all()
    post = dataStructure.objects.filter(slug=slug).first()
    context = {'course':post,'allPost':allPost}
    return render(request,'course/coursepage.html',context)

    

def OopHome(request):
    allPost = Oop.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/chapter.html',context)


def OopContent(request,slug):
    allPost = Oop.objects.all()
    post = Oop.objects.filter(slug=slug).first()
    context = {'course':post,'allPost':allPost}
    return render(request,'course/coursepage.html',context)
 

def DBMSHome(request):
    print('\n\nhello\n\n')
    allPost = DBMS.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/chapter.html',context)


def DBMSContent(request,slug):
    print("i am working\n\n")
    allPost = DBMS.objects.all()
    post = DBMS.objects.filter(slug=slug).first()
    context = {'course':post,'allPost':allPost}
    return render(request,'course/coursepage.html',context)
 
def DEHome(request):
    allPost = digitalElectronics.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/chapter.html',context)


def DEContent(request,slug):
    allPost = digitalElectronics.objects.all()
    post = digitalElectronics.objects.filter(slug=slug).first()
    context = {'course':post,'allPost':allPost}
    return render(request,'course/coursepage.html',context)
 
def MathsHome(request):
    allPost = Maths.objects.all()
    context = {'allPost':allPost}
    return render(request,'course/chapter.html',context)


def MathsContent(request,slug):
    allPost = Maths.objects.all()
    post = Maths.objects.filter(slug=slug).first()
    context = {'course':post,'allPost':allPost}
    return render(request,'course/coursepage.html',context)
 
    