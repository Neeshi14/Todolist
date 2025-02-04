from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def todolist(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(name= task_name)
        return redirect('todolist')

    tasks = Task.objects.all()

    queryset ={'tasks' : tasks}
    return render(request , 'index.html' , queryset)    


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todolist')




def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todolist')