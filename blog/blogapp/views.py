from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def index(request):
    blog= Blog.objects.all()
    arguments={
        'name':'Bony',
        'blog': blog
    }
    return render(request,'index.html',arguments)

def slug(request, slug):
    blog= Blog.objects.filter(slug=slug)

    arguments={
        'name':'Bony',
        'blog': blog
    }
    return render(request,'bolg_template.html',arguments)

def dashboard(request):
    blog= Blog.objects.all

    arguments={
        
        'blog': blog
    }
    return render(request,'dashboard.html',arguments)

def login(request):
    if request.method=='POST':
        username=request.POST['userid']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/dashboard")
        else:
            messages.error(request,'inavlid')
            return redirect("/login")
   
    else:
        return render(request,'sigin.html')

def logout(request):

    auth.logout(request)
    return redirect("/")

def add(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        slug=request.POST['slug']
        blog_add=Blog(title=title,body=content,slug=slug)
        blog_add.save()
        return redirect("/dashboard")
    else:
        return render(request,'addHtml.html')

def delete(request):
    if request.method=='POST':
         blog_id=request.POST['id']
         Blog.objects.filter(id=blog_id).delete()
         return redirect('/dashboard')
    else:
         return render(request,'addHtml.html')

def update(request,id):
    if request.method=='POST':
         #blog_id=request.POST['id']
         title=request.POST['title']
         content=request.POST['content']
         slug=request.POST['slug']
         Blog.objects.filter(id=id).update(title=title,body=content,slug=slug)
         return redirect('/dashboard')
    else:
         print(id)
         Blog_up=Blog.objects.filter(id=id)
         arguments={
             
            'blogup':Blog_up
         }
         return render(request,'update.html',arguments)
