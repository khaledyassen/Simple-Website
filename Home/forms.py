from django.contrib.auth.models import User
from django.contrib.auth import forms

class register_page(forms.UserCreationForm):

  class Meta:
    model=User
    fields=['username','email','password1','password2']
