from django.urls import path 
from .views import task, post_date

app_name ='tasks'

urlpatterns = [
    path('date/',task,name="date"),
    path('<str:date>/',post_date,name="post_date")
]