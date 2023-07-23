# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from livestockapp.models import Category
from django.utils import timezone
import datetime


date = datetime.datetime.now() 


# Create your views For Category.
def cat_insert(request):
    if request.method == "POST":
        name = request.POST['name']
        if name == "":
            return render(request,'animal_category/insert.html', {'error': True})    
        description = request.POST['description']                 
        ins=Category(
            name=name, 
            description=description, 
            created_on=date)
        ins.save()
        return redirect(reverse('show'))
    return render(request,'animal_category/insert.html')

def cat_show(request):
    allTasks = Category.objects.all()
    context = {'tasks': allTasks}
    return render(request,'animal_category/list.html', context)

#This Function Will Edit/Update in Category
def cat_delete(request,category_id):
    delete = Category.objects.get(category_id=category_id)
    delete.delete()
    return redirect('/show')

 #This Function Will Edit/Update in Category
def cat_edit(request , category_id):
    cat = Category.objects.get(category_id=category_id)
    return render(request, 'animal_category/update.html',{'cat':cat})

def cat_updated(request, category_id):
    if request.method == 'POST':
        category_id = request.POST['category_id']
        name = request.POST['name']
        if request.POST.get('name')=="":
            return render(request, 'animal_category/update.html',{'error':True})
        description = request.POST['description']
        if request.POST.get('description')=="":
              return render(request,'animal_category/insert.html', {'error1': True})  
        else:  
            edit = Category.objects.get(category_id = category_id)      
            edit.name = name  
            edit.description = description    
            edit.updated_on = date       
            edit.save()
            return redirect(reverse('show'))       