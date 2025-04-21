from django.shortcuts import render,redirect,get_object_or_404 # type: ignore
from .models import Student

# Create your views here.
def home(request):
    context={'pages':'home'}
    return render(request,'students/home.html',context)
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
