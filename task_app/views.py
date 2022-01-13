from django.shortcuts import redirect, render
from task_app.forms import TaskForm, UserForm
from django.views import View
from task_app.models import Task



# Create your views here.
class CreateUser(View):
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create-task/")
        else:
            form = UserForm()
        return render(request,'user.html',{'form':form})  
    

    def get(self,request):
        form = UserForm()
        return render(request,'user.html',{'form':form})


class CreateTask(View):
    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show-task/")
        else:
            form = TaskForm()
        return render(request,'task.html',{'form':form})  
    
   
    def get(self,request):
        form = TaskForm()
        return render(request,'task.html',{'form':form})


class ShowTask(View):
    def get(self,request):
        tasks = Task.objects.all()
        return render(request,'display.html',{'tasks':tasks})  
   


class UpdateTask(View):
    def get(self,request,id):
        model_instance = Task.objects.get(pk=id)
        form = TaskForm(instance=model_instance)
        return render(request,'update.html',{'form':form})              
        
    def post(self,request,id):
        model_instance = Task.objects.get(pk=id)
        form = TaskForm(request.POST,instance=model_instance) 
        if form.is_valid():
            form.save()
            return redirect('show-task')
        else:
            form = TaskForm()
        return render(request,'update.html',{'form':form}) 

class DeleteTask(View):
    def get(self,request,id):
        obj = Task.objects.get(pk=id) 
        obj.delete()  
        return redirect('show-task')        
            
        




         


