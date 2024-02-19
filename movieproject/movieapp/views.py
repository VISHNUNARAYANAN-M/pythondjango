from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import MovieForm
# Create your views here.
def index(request):
    details = movie.objects.all()
    context={
        'movielist':details
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    id=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'id':id})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        item=movie(name=name,desc=desc,year=year,img=img)
        item.save()
        return redirect('/')

    return render(request,'add.html')
def update(request,id):
    id=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'id':id})
def delete(request,id):
    if request.method=='POST':
        id=movie.objects.get(id=id)
        id.delete()
        return redirect('/')
    return render(request,'delete.html')
