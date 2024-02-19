from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Todolistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'details'
class TodoDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'obj'

class TodoUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'obj'
    fields=('task','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class TodoDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')

def add(request):
    details=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(task=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'details':details})
def delete(request,id):
    id = Task.objects.get(id=id)
    if request.method=='POST':
        id.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    id=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'id':id})

