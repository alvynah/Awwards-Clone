from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','project_image','project_url','technologies')
    
