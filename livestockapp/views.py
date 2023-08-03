# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from livestockapp.models import Category,Animal_profile
from django.utils import timezone
from datetime import datetime


x = datetime.now() 
date = x.strftime('%Y-%m-%d')

#datetime.datetime.strptime('5/10/1955', '%d/%m/%Y').strftime('%Y-%m-%d')


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
def insert_animal_profile(request):
    
    if request.method == "POST":
       
        token_no = request.POST['token_no']
        name = request.POST['ani_name']
        pragnant_val = request.POST['pragnant_val']
        is_pragnant = int(pragnant_val)
        color = request.POST['color']
        category_id = request.POST['category_id']
        weight = request.POST['weight']
        purchase_price = request.POST['purchase_price']
        purchased_on = request.POST['purchased_on']
        
        
        purchased_on = datetime.strptime(purchased_on,  '%Y-%m-%d')
        print(purchased_on)
        purchased_by = request.POST['purchased_by']
        date_of_birth = request.POST['date_of_birth']
        if date_of_birth == '':
            date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        gender = request.POST['gender']
        pragnancy_start_date = request.POST['pragnancy_start_date']
        if pragnancy_start_date == '':
            pragnancy_start_date = None
        else:
            pragnancy_start_date = datetime.strptime(pragnancy_start_date,  '%Y-%m-%d')
        pragnancy_end_date = request.POST['pragnancy_end_date']  
        if pragnancy_end_date == '':
            pragnancy_end_date = None
        else:
            pragnancy_end_date = datetime.strptime(pragnancy_end_date,  '%Y-%m-%d')
        status = request.POST['status_val']
        description = request.POST['description'] 
        
        ani=Category.objects.all()
        if token_no == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error2': True , 'ani': ani,'date':date})
        if name == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error3': True, 'ani': ani,'date':date})    
        if color == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error4': True, 'ani': ani,'date':date})    
        if category_id == "":
             return render(request,'animal_profile/insert_animal_profile.html', {'error5': True, 'ani': ani,'date':date})    
        if purchase_price == '':
            purchase_price = 0
        if gender == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error6': True, 'ani': ani,'date':date})  
        if is_pragnant == 1 and pragnancy_start_date == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error8': True, 'ani': ani,'date':date})    
        if status == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error9': True, 'ani': ani,'date':date}) 
        
        ins=Animal_profile(token_no=token_no,name=name,color=color,weight=weight,
                           category_id=category_id,
                           purchase_price=purchase_price,
                           purchased_on=purchased_on,
                           purchased_by=purchased_by,
                           date_of_birth=date_of_birth,
                           gender=gender,
                           is_pragnent=is_pragnant,
                           pragnancy_start_date=pragnancy_start_date,
                           pragnancy_end_date=pragnancy_end_date,
                           status=status,
                           updated_by=1,
                           description=description)
            
        ins.save()
        
        return redirect(reverse('list_animal_profile'))
    ani=Category.objects.all()
    return render(request,'animal_profile/insert_animal_profile.html', {'ani': ani ,'date':date } )

def list_animal_profile(request):
    allTasks = Animal_profile.objects.all()
    context = {'animal_pro': allTasks}
    return render(request,'animal_profile/list_animal_profile.html', context)

#This Function Will Edit/Update in Animal profile
def animal_pro_delete(request,id):
    delete = Animal_profile.objects.get(id=id)
    delete.delete()
    return redirect('/list_animal_profile')

 #This Function Will Edit/Update in Animal profile
def animal_pro_edit(request , id):
    animal = Animal_profile.objects.get(id=id)
    ani=Category.objects.all()
    return render(request, 'animal_profile/update_animal_profile.html',{'animal':animal,'ani': ani})

def update_animal(request, id):
    if request.method == 'POST':
        id = request.POST['id']
        token_no = request.POST['token_no']
        name = request.POST['name']
        color = request.POST['color']
        weight = request.POST['weight']
        category_id = request.POST['category_id']
        purchase_price = request.POST['purchase_price']
        purchased_on = request.POST['purchased_on']
        purchased_by = request.POST['purchased_by']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        pragnant_val = request.POST['is_pragnant']
        is_pragnant = int(pragnant_val)
        pragnancy_start_date = request.POST['pragnancy_start_date']
        pragnancy_end_date = request.POST['pragnancy_end_date']
        status = request.POST['status']
        description = request.POST['description']

        anim=Category.objects.all()
        if token_no == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error2': True , 'anim': anim})
        if name == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error3': True, 'anim': anim})    
        if color == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error4': True, 'anim': anim})    
        if category_id == "":
             return render(request,'animal_profile/update_animal_profile.html', {'error5': True, 'anim': anim})    
        if purchase_price == '':
            purchase_price = 0
        if gender == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error6': True, 'anim': anim})  
        if is_pragnant == 1 and pragnancy_start_date == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error8': True, 'anim': anim})    
        if status == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error9': True}) 
       
        else:  
            edit = Animal_profile.objects.get(id = id)  
            edit.token_no = token_no    
            edit.name = name 
            edit.color = color 
            edit.weight = weight
            edit.category_id = category_id
            edit.purchase_price = purchase_price
            edit.purchased_on = purchased_on
            edit.purchased_by = purchased_by
            edit.date_of_birth = date_of_birth
            edit.gender = gender
            edit.is_pragnent=is_pragnant,
            edit.pragnancy_start_date = pragnancy_start_date
            edit.pragnancy_end_date = pragnancy_end_date
            edit.status=status
            edit.description = description    
            edit.updated_on = date       
            edit.save()
            return redirect(reverse('list_animal_profile')) 
    animals=Category.objects.all()
    return render(request,'animal_profile/update_animal_profile.html', {'animals': animals ,'date':date } )
