from django.shortcuts import render
#from django.http import HttpResponse

def home_request(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def course(request):
    return render(request,'course.html')
def single(request):
    return render(request,'single.html')
def teacher(request):
    return render(request,'teacher.html')