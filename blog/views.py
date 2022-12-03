from django.shortcuts import render,HttpResponse
from blog.models import blog

# Create your views here.
def blogHome(request):
    allPost = blog.objects.all()
    context = {'allPost':allPost}
    return render(request,'blog/blogHome.html',context)


def blogPost(request,slug):
    post = blog.objects.filter(slug=slug).first()
    allPost = blog.objects.all()
    context = {'blog':post,'allPost':allPost}
    return render(request,'blog/blogPage.html',context)