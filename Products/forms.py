from django import forms
from .models import BuyingProducts

class BuyingProducts_forms(forms.ModelForm):
  class Meta:
    model=BuyingProducts
    fields='__all__'
