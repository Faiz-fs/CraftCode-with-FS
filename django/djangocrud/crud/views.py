from django.shortcuts import render,redirect
from crud.forms import StudentForm
from crud.models import Student

# Create your views here.

def index(request):
    data=Student.objects.all()
    return render(request,'index.html',{"data":data})

def create(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form=StudentForm
    content={'form':form}
    return render(request,'create.html',content)

def update(request,id):
    data=Student.objects.get(id=id)
    print(data)
    form = StudentForm(request.POST or None,instance=data)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('read')
    context={'form':form}
    return render(request,'update.html',context)

def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('read')
    #return render(request,'delete.html')