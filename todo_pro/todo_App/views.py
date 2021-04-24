from django.shortcuts import render, redirect

# Create your views here.
from todo_App.models import Task
from.forms import Todoforms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.urls import reverse_lazy

class TaskListview(ListView):
    model = Task
    template_name = 'taskview.html'
    context_object_name = 'key'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('cbvtask')


def show(request):
    task_obj = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        t = Task(name=name, priority=priority,date=date)
        t.save()


    return render(request,'taskview.html',{'key':task_obj})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete_task.html',{'task_key':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})