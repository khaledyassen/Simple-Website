from django import forms
from django.db.models import fields
from .models import *

class customerForm(forms.ModelForm):
  class Meta:
    model=Customer
    fields='__all__'
    exclude=['user']

class contactUSForm(forms.ModelForm):
  class Meta:
    model=contactUS
    fields='__all__'