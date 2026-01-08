from django import forms
# form . model import *
from dashboard import models
# from dashboard.views import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NotesForm(forms.ModelForm):
    class Meta:
        model=models.Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type='date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model=models.Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']

class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter Your Search : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo 
        fields=['title','is_finished']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']



        