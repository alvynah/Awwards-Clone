from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponseRedirect


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
   users = User.objects.exclude(id=request.user.id)
   profiles=Profile.objects.all()
   projects=Project.objects.all()
   
   if request.method=='POST':
         form=UploadProjectForm(request.POST, request.FILES)
         if form.is_valid():
               project=form.save(commit=False)
               project.user=request.user.profile
               project.save()
               return HttpResponseRedirect(request.path_info)
   else:
      form=UploadProjectForm()
       
          
   params={
       'users':users,
       'profiles':profiles,
       'projects':projects,
       'form':form,
    }
   return render(request,'awwards/index.html',params) 