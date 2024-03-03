from django.shortcuts import render
from movieapp.models import Movies,Category
from django.db.models import Q
# Create your views here.
def searchresult(request):
    categories = Category.objects.all()

    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Movies.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        category=Category.objects.all().filter(Q(name__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies,'category':category,'categories':categories})
