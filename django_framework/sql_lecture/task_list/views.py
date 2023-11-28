from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

task_list = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "task_list/index.html", {
        "task_list": task_list
    })    
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            task_list.append(task)
            return HttpResponseRedirect(reverse("task_list:index"))
        else:
            return render(request, "task_list/add.html",{
              "form": form  
            })
            
    return render(request, "task_list/add.html", {
        "form": NewTaskForm()
    })