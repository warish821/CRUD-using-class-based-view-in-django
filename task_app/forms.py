from task_app.models import  Task, Users
from . import forms
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
    

    

    

