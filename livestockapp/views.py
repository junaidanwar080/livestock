# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from livestockapp.models import Category,Animal_profile
from django.utils import timezone
import datetime


date = datetime.datetime.now() 


# Create your views For Category.
def cat_insert(request):
    if request.method == "POST":
        name = request.POST['cat_name']
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
        




        
# Create your views For Animal Profile.
def animal_pro_insert(request):
    if request.method == "POST":
        token_no = request.POST['token_no']
        if token_no == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error2': True})
        name = request.POST['ani_name']
        if name == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error3': True})    
        color = request.POST['color']
        if color == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error4': True})    
        weight = request.POST['weight']
        category_id = request.POST['category_id']
        if category_id == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error5': True})    
        Purchase_price = request.POST['Purchase_price']
        Purchased_date = request.POST['Purchased_date']    
        Purchased_by = request.POST['Purchased_by']    
        date_of_birth = request.POST['date_of_birth']    
        gender = request.POST['gender']
        if gender == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error6': True})    
        is_pragnent = request.POST['is_pragnent']
        if is_pragnent == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error7': True})    
        pregnancy_start_date = request.POST['pregnancy_start_date']
        if pregnancy_start_date == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error8': True})    
        pregnancy_end_date = request.POST['pregnancy_end_date']
        is_active = request.POST['is_active']
        if is_active == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error9': True})        
        description = request.POST['description']                 
        ins=Animal_profile(
            token_no=token_no,
            name=name,
            color=color,
            weight=weight,
            category_id_id=category_id,
            Purchase_price=Purchase_price,
            Purchased_date=Purchased_date,
            Purchased_by=Purchased_by,
            date_of_birth=date_of_birth,
            gender=gender,
            is_pragnent=is_pragnent,
            pregnancy_start_date=pregnancy_start_date,
            pregnancy_end_date=pregnancy_end_date,
            is_active=is_active,
            description=description, 
            )
        ins.save()
        ani=Category.objects.all()
        return redirect(reverse('animal_pro_show'), { "ani": ani})
    return render(request,'animal_profile/insert_animal_profile.html', )

def animal_pro_show(request):
    allTasks = Animal_profile.objects.all()
    context = {'animal_pro': allTasks}
    return render(request,'animal_profile/list_animal_profile.html', context)

#This Function Will Edit/Update in Animal profile
def animal_pro_delete(request,id):
    delete = Animal_profile.objects.get(id=id)
    delete.delete()
    return redirect('/animal_pro_show')

 #This Function Will Edit/Update in Animal profile
def animal_pro_edit(request , id):
    cat = Animal_profile.objects.get(id=id)
    return render(request, 'animal_profile/update_animal_profile.html',{'cat':cat})

def animal_pro_updated(request, id):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        if request.POST.get('name')=="":
            return render(request, 'animal_profile/update_animal_profile.html',{'error':True})
        description = request.POST['description']
        if request.POST.get('description')=="":
              return render(request,'animal_profile/update_animal_profile.html', {'error1': True})  
        else:  
            edit = Animal_profile.objects.get(id = id)      
            edit.name = name  
            edit.description = description    
            edit.updated_on = date       
            edit.save()
            return redirect(reverse('animal_pro_show')) 