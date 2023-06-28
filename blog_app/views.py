from django.shortcuts import render

from blog_app.models import Post,Category



# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]

    cats= Category.objects.all()


    return render (request,'index.html',{'posts':posts,'cats':cats})

def post(request,url):
    posts= Post.objects.get(url=url)


    return render(request,'post.html',{'posts':posts})

def cats(request,url):
    cats= Category.objects.get(url=url)


    return render(request,'cat.html',{'cats':cats})

