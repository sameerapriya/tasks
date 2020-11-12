from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=255)
    task_from = models.DateTimeField()
    task_to = models.DateTimeField()
    details = models.TextField(blank=True,null=True,max_length=1000)
    STATUS = (('active', 'Is Active'), ('complete', 'Complete'),('not_active', 'N.A'))
    status = models.CharField(choices=STATUS, default='active', max_length=20, blank=True)
