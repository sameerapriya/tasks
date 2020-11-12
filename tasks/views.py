from django.shortcuts import render, redirect
from .forms import TaskForm
import datetime
from .models import Task
from django.db.models import Q
# Create your views here.


def task(request):
    """ This method handles what has to be done with the date provided by the user."""

    if request.method == "GET":
        if 'date' in request.GET: # checking if the parameter has been passed 
            date = request.GET.get('date')
            return redirect('tasks:post_date', date=date) #passing the value in with an argument
        else :
            error = "Please enter a valid date."
            return render(request,"tasks/date.html",{'error':error}) # if format is incorrect error would be thrown.
        return render(request,"tasks/date.html") # rendering the html 

def post_date(request, date):
    """handles aftermath of which tasks fall into particular date"""
    date = date.split('-') # the date i.e., passed is 2020-03-04 , to pass it as a date object , the whole logic has been written.
    date = "".join(date)
    date = datetime.datetime.strptime(date, "%Y%m%d").date()
    tasks = Task.objects.filter(Q(task_from__date__lte=date) & Q(task_to__date__gte=date)
    ) # condition to see if it falls between the particular date range 

    if tasks.count() >= 1: # if yes , the task objects are passed 
        return render(request, "tasks/task_details.html",{'tasks':tasks})   

    else: # else a provision to create a new task would be provided 
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('tasks:date')
            else:
                return render(request,"tasks/task_post.html",{'form':form})
        return render(request,"tasks/task_post.html",{'form':TaskForm()})

