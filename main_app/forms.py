from django.forms import ModelForm
from .models import Feeding
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput): 
    input_type = 'time'

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
    widgets = { 
            'date' : DateInput(),
            'time' : TimeInput(), 
        }