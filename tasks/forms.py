from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """ Form for the Model TASK """
    task_from = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],label='Start Date and Time')
    task_to = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],label='End Date and Time')
    class Meta:
        model = Task
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        task_from = cleaned_data.get('task_from')
        task_to = cleaned_data.get('task_to')
        if task_from and task_to:
            if task_from > task_to : # to check if date start and end dates of the provided in a correct manner 
                raise forms.ValidationError('Please make sure the starting date and time of the task is accurate')
