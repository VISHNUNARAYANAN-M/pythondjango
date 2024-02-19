from django.shortcuts import render
from .models import place,team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    member=team.objects.all()
    return render(request,'index.html',{'obj':obj,'member':member})
