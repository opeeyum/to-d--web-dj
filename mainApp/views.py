from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from .forms import getTaskForm

from .models import userTask

#Views

def index(request):
    if request.user.is_authenticated:
        return redirect('mainApp:create-task')
    return render(request, "mainApp/tasks.html", {})

@login_required(login_url='accounts:login')
def create_task(request):
    if request.method == 'POST':
        form = getTaskForm(request.POST)
        print("data arived")
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
        messages.success(request, "Task added successfully!")
        return redirect('mainApp:index')
    
    else:
        form = getTaskForm()
    
    context = {
        'form': form,
        'all_tasks': userTask.objects.filter(host=request.user),
        'task_count': userTask.objects.filter(host__id=request.user.id).count(),
    }

    return render(request, 'mainApp/tasks.html', context)


def delete_task(request, id):
    task_instance = userTask.objects.get(pk=id)
    task_instance.delete()
    return redirect('mainApp:create-task')