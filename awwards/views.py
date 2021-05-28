from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
def signup_view(request):
   if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)


            return redirect('welcome')
   else:
        form = SignUpForm()
   return render(request, 'registration/signup.html', {'form': form})
    

def welcome(request):
   return render(request,'awwards/index.html') 