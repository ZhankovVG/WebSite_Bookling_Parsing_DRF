from django import forms
from .models import *


class CallbackForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ('name', 'phone_number')