from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from . import models


def home(request):
    all_todo = models.Tods.objects.all().order_by("-do_date")
    return render(request, 'polls/index.html', {'all_todo': all_todo})


def new_add(request):
    title = request.POST.get('Title')
    details = request.POST.get('details')
    models.Tods.objects.create(Title=title, details=details)
    return HttpResponseRedirect('/polls')


def delete_todo(request, todo_id):
    models.Tods.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/polls')


def edit_todo(request, todo_id):
    all_todo = models.Tods.objects.get(id=todo_id)
    return render(request, 'polls/update.html', {'all_todo': all_todo})


def update_todo(request, todo_id):
    title = request.POST.get('Title')
    details = request.POST.get('details')
    models.Tods.objects.filter(id=todo_id).update(Title=title, details=details)
    return HttpResponseRedirect('/polls')


def detail_todo(request, todo_id):
    all_todo = models.Tods.objects.get(id=todo_id)
    return render(request, 'polls/details.html', {'all_todo': all_todo})
