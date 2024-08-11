from django.shortcuts import render, redirect

from todo.forms import TodoForm
from todoapp.models import TodoModel


def index(request):
    return render(request, 'index.html')


def form(request):
    form = TodoForm()
    if request.method == "POST":
        data = TodoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('view')

    return render(request, 'form.html', {'form': form}, )


def view(request):

    info = TodoModel.objects.all()
    return render(request, 'view.html', {'info': info})


def update(request,id):
    data = TodoModel.objects.get(id=id)
    form = TodoForm(instance=data)
    if request.method == "POST":
        data = TodoForm(request.POST, instance=data)
        if data.is_valid():
            data.save()
            return redirect('view')
    return render(request, 'update.html', {'form': form})

def delete(request,id):
    data=TodoModel.objects.get(id=id)
    data.delete()
    return redirect('view')