from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.admin import UserAdmin



# Create your views here.

def index(request):
    return render(request,'index.html')

def regist(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/regist.html',{'form':form})

def login(request):
    '''
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect('profile')
    else:
        form=AuthenticationForm()'''
    return render(request,'registration/login.html')


def profile(request):
    return render(request,'profile.html')
