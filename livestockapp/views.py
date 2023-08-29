# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from livestockapp.models import Category,Animal_profile,PregnancyDetails
from django.utils import timezone
from datetime import datetime


x = datetime.now() 
date = x.strftime('%Y-%m-%d')

#------------Create your views For Category---------------
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

#---------------Delete Category--------------------
def cat_delete(request,category_id):
    delete = Category.objects.get(category_id=category_id)
    delete.delete()
    return redirect('/show')

 #----------------Edit Category-------------------
def cat_edit(request , category_id):
    cat = Category.objects.get(category_id=category_id)
    return render(request, 'animal_category/update.html',{'cat':cat})
#-----------------Update Category-----------------
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
# ---------------Animal Profile--------------
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
#----------Delete Animal profile---------------
def animal_pro_delete(request,animal_id):
    delete = Animal_profile.objects.get(animal_id=animal_id)
    delete.delete()
    return redirect('/list_animal_profile')
#----------Edit Animal profile-----------------
def animal_pro_edit(request , animal_id ):
    animal = Animal_profile.objects.get(animal_id=animal_id)
    ani=Category.objects.all()
    return render(request, 'animal_profile/update_animal_profile.html',{'animal':animal,'ani': ani})
#-----------Update Animal Profile--------------
def update_animal(request, animal_id):
    if request.method == 'POST':
        animal_id = request.POST['animal_id']
        token_no = request.POST['token_no']
        name = request.POST['ani_name']
        color = request.POST['color']
        weight = request.POST['weight']
        category_id = request.POST['category_id']
        purchase_price = request.POST['purchase_price']
        purchased_on = request.POST['purchased_on']
        if purchased_on == '':
            purchased_on = None
        else:
            purchased_on = datetime.strptime(purchased_on,  '%Y-%m-%d')
        purchased_by = request.POST['purchased_by']
        date_of_birth = request.POST['date_of_birth']
        if date_of_birth == '':
            date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        gender = request.POST['gender']
        is_pragnant = request.POST['pragnant_val']
        
        pragnancy_start_date = request.POST['pragnancy_start_date']
        if gender == 'male' or is_pragnant == '0':
            pragnancy_start_date = None
        else:
            pragnancy_start_date = datetime.strptime(pragnancy_start_date,  '%Y-%m-%d')
        pragnancy_end_date = request.POST['pragnancy_end_date']
        if gender == 'male'or is_pragnant == '0':
            pragnancy_end_date = None
        else:
            pragnancy_end_date = datetime.strptime(pragnancy_end_date,  '%Y-%m-%d')
        status = request.POST['status_val']
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
            edit.category_id =category_id
            edit.purchase_price = int(purchase_price)
            edit.purchased_on = purchased_on
            edit.purchased_by = purchased_by
            edit.date_of_birth = date_of_birth
            edit.gender = gender
            edit.is_pragnent=is_pragnant
            edit.pragnancy_start_date = pragnancy_start_date
            edit.pragnancy_end_date = pragnancy_end_date
            edit.status=status
            edit.description = description  
            edit.updated_on = date    
            edit.save()
            return redirect(reverse('list_animal_profile')) 
    animals=Category.objects.all()
    return render(request,'animal_profile/update_animal_profile.html', {'animals': animals ,'date':date } )


#------------------ Insert Pregnancy Details-----------------------------

def insert_pregnency_detail(request):   
    if request.method == "POST":     
        animal_id = request.POST['animal_id']
        start_date = request.POST['start_date']
        if start_date == '':
            start_date = None
        else:
            start_date = datetime.strptime(start_date,  '%Y-%m-%d')
        expected_end_date = request.POST['expected_end_date']
        if expected_end_date == '':
            expected_end_date = None
        else:
            expected_end_date = datetime.strptime(expected_end_date, '%Y-%m-%d')
        is_pregnancy_confirmed = request.POST['is_pregnancy_confirmed']
        pregnancy_checked_on = request.POST['pregnancy_checked_on']
        pregnancy_checked_on = datetime.strptime(pregnancy_checked_on,  '%Y-%m-%d')
        is_delivery_completed = request.POST['is_delivery_completed']
        actual_delivery_date = request.POST['actual_delivery_date']
        if actual_delivery_date == '':
            actual_delivery_date = None
        else:
            actual_delivery_date = datetime.strptime(actual_delivery_date,  '%Y-%m-%d')
        is_miscarriage = request.POST['is_miscarriage']       
        miscarriage_date = request.POST['miscarriage_date']
        if miscarriage_date == '':
            miscarriage_date = None
        else:
            miscarriage_date = datetime.strptime(miscarriage_date,  '%Y-%m-%d')
        infartility = request.POST['infartility']  
        pragnant_val = request.POST['pragnant_val']
        is_pragnant = int(pragnant_val)  
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
        description = request.POST['description']        
        det=Animal_profile.objects.all()
        if animal_id == "":
            return render(request,'pregnancy_details/insert_pregnency_detail.html', {'error2': True , 'det': det,'date':date})
        
        ins=PregnancyDetails(animal_id=animal_id,
                             start_date=start_date,expected_end_date=expected_end_date,
        is_pregnancy_confirmed=is_pregnancy_confirmed,
        pregnancy_checked_on=pregnancy_checked_on,
        is_delivery_completed=is_delivery_completed,
        actual_delivery_date=actual_delivery_date,
        is_miscarriage=is_miscarriage,
        miscarriage_date=miscarriage_date,
        infartility=infartility,
        is_pragnant=is_pragnant,
        pragnancy_start_date=pragnancy_start_date,
        pragnancy_end_date=pragnancy_end_date,
        description=description)
        ins.save()   
        return redirect(reverse('list_pregnency_detail'))
    det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/insert_pregnency_detail.html', {'det': det ,'date':date } )

#-----------List Pregnancy Detail-----------------

def list_pregnency_detail(request):
    allTasks = PregnancyDetails.objects.all()
    context = {'animal_det': allTasks}
    return render(request,'pregnancy_details/list_pregnency_detail.html', context)

#----------Delete Pregnancy Detail---------------

def animal_det_delete(request,Pregnancy_id):
    delete = PregnancyDetails.objects.get(Pregnancy_id=Pregnancy_id)
    delete.delete()
    return redirect('/list_pregnency_detail')

#----------Edit Pregnancy Detail-----------------

def animal_det_edit(request , Pregnancy_id ):
    detail = PregnancyDetails.objects.get(Pregnancy_id=Pregnancy_id)
    det=Animal_profile.objects.all()
    return render(request, 'pregnancy_details/update_pregnency_detail.html',{'detail':detail,'det': det })

#-----------------Update Pregnancy Detail--------------------------#

def update_pregnency_detail(request, Pregnancy_id):
    if request.method == 'POST':
       animal_id = request.POST['animal_id']
       start_date = request.POST['start_date']
       if start_date == '':
            start_date = None
       else:
            start_date = datetime.strptime(start_date,  '%Y-%m-%d')
       expected_end_date = request.POST['expected_end_date']
       if expected_end_date == '':
            expected_end_date = None
       else:
           expected_end_date = datetime.strptime(expected_end_date,  '%Y-%m-%d')
       is_pregnancy_confirmed = request.POST['is_pregnancy_confirmed']
       pregnancy_checked_on = request.POST['pregnancy_checked_on']
       if pregnancy_checked_on == '':
           pregnancy_checked_on = None
       else:
           pregnancy_checked_on = datetime.strptime(pregnancy_checked_on,  '%Y-%m-%d')
       is_delivery_completed = request.POST['is_delivery_completed']
       actual_delivery_date = request.POST['actual_delivery_date']
       if actual_delivery_date == '':
           actual_delivery_date = None
       else:
           actual_delivery_date = datetime.strptime(actual_delivery_date,  '%Y-%m-%d')
       is_miscarriage = request.POST['is_miscarriage']       
       miscarriage_date = request.POST['miscarriage_date']
       if miscarriage_date == '':
           miscarriage_date = None
       else:
           miscarriage_date = datetime.strptime(miscarriage_date,  '%Y-%m-%d')
       infartility = request.POST['infartility']
       is_pragnant = request.POST['pragnant_val']
        
       pragnancy_start_date = request.POST['pragnancy_start_date']
       if pragnancy_start_date == '' :
            pragnancy_start_date = None
       else:
            pragnancy_start_date = datetime.strptime(pragnancy_start_date,  '%Y-%m-%d')
       pragnancy_end_date = request.POST['pragnancy_end_date']
       if pragnancy_end_date == '':
           pragnancy_end_date = None
       else:
           pragnancy_end_date = datetime.strptime(pragnancy_end_date,  '%Y-%m-%d')


       pragnancy_count = PregnancyDetails.objects.filter(is_pragnent = 1).count()
       
       print(pragnancy_count)

       
       description = request.POST['description']        
       det=Animal_profile.objects.all()
       if animal_id == "":
           return render(request,'pregnancy_details/update_pregnency_detail.html', {'error2': True , 'det': det,'date':date})
       else:
           edit = PregnancyDetails.objects.get(Pregnancy_id = Pregnancy_id)  
           edit.animal_id = animal_id
           edit.start_date = start_date
           edit.expected_end_date = expected_end_date
           edit.is_pregnancy_confirmed = is_pregnancy_confirmed
           edit.pregnancy_checked_on = pregnancy_checked_on
           edit.is_delivery_completed =is_delivery_completed  
           edit.actual_delivery_date=actual_delivery_date        
           edit.is_miscarriage = is_miscarriage
           edit.miscarriage_date = miscarriage_date
           edit.infartility = infartility
           edit.is_pragnent=is_pragnant
           edit.pragnancy_start_date = pragnancy_start_date
           edit.pragnancy_end_date = pragnancy_end_date
           edit.description = description 
           edit.updated_on = date  
           edit.pragnancy_count = pragnancy_count  
           edit.save()
          
           return redirect(reverse('list_pregnency_detail')) 
    det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/update_pregnency_detail.html', {'det': det ,'date':date } )

