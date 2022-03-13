from django import forms

from .models import userTask

class getTaskForm(forms.ModelForm):
    class Meta:
        model = userTask
        fields = ['task',]