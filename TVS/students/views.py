from django.shortcuts import render,redirect,get_object_or_404 # type: ignore
from .models import Student
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required# type: ignore

# Create your views here.
def home(request):
    student=Student.objects.all()
    context={'pages':'home',
             'students':student}
    return render(request,'students/home.html',context)
@login_required(login_url='/login_page/')
def index(request):
    if request.method=="POST":
        data=request.POST
        student_name=data.get('student_name')
        student_class=data.get('student_class')
        student_image=request.FILES.get('student_image')
        
        Student.objects.create(
            student_name=student_name,
            student_class=student_class,
            student_image=student_image
        )
        return redirect('/index/')
    QuerySet=Student.objects.all()
    if request.GET.get('Search'):
        QuerySet=QuerySet.filter(student_name__icontains=request.GET.get('Search'))
    context={
        'pages':'students',
        'students':QuerySet
    }
    return render(request,'students/index.html',context)

def delete_record(request,id):
    if request.method=="POST":
        data=get_object_or_404(Student,id=id)
        data.delete()
    return redirect('/index/')
def update_record(request,id):
    data=get_object_or_404(Student,id=id)
    if request.method=="POST":
        querySet=request.POST
        student_name=querySet.get('student_name')
        student_class=querySet.get('student_class')
        student_image=request.FILES.get('student_image')
        
        data.student_name=student_name
        data.student_class=student_class
        if student_image:
            data.student_image=student_image
        data.save()
        return redirect('/index/')
    context={'student':data}
    return render(request,'students/update.html',context)

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Credentials")
            return redirect('/login_page/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Credentials")
            return redirect('/login_page/')
        else:
            login(request,user)
            return redirect('/index/')         
    return render(request,'students/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page/')
def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return render(request,'students/register.html')
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.set_password(password)
        user.save()
        messages.success(request,'User created successfully')
        return redirect('/login_page/')
    
    return render(request, 'students/register.html')
            