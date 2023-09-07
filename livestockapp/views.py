# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from livestockapp.models import Category, Animal_profile, PregnancyDetails, UserProfile
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User , Group
from django.db.models import Count

x = datetime.now() 
date = x.strftime('%Y-%m-%d')

# -----------------------------------------------------------------------------------------------------
# Catergory Insert
# -----------------------------------------------------------------------------------------------------

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
# -----------------------------------------------------------------------------------------------------
# List Category 
# -----------------------------------------------------------------------------------------------------
def cat_show(request):
    allTasks = Category.objects.all()
    context = {'tasks': allTasks}
    return render(request,'animal_category/list.html', context)
# -----------------------------------------------------------------------------------------------------
# Delete Category
# -----------------------------------------------------------------------------------------------------
def cat_delete(request,category_id):
    delete = Category.objects.get(category_id=category_id)
    delete.delete()
    return redirect('/show')
# -----------------------------------------------------------------------------------------------------
# Edit Category
# -----------------------------------------------------------------------------------------------------
def cat_edit(request , category_id):
    cat = Category.objects.get(category_id=category_id)
    return render(request, 'animal_category/update.html',{'cat':cat})
# -----------------------------------------------------------------------------------------------------
# Update Category
# -----------------------------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------------------              
# Insert Animal Profile
# -----------------------------------------------------------------------------------------------------
def insert_animal_profile(request):   
    if request.method == "POST":     
        token_no = request.POST['token_no']
        name = request.POST['ani_name']
        color = request.POST['color']
        category_id = request.POST['category_id']
        weight = request.POST['weight']
        purchase_price = request.POST['purchase_price']
        purchased_on = request.POST['purchased_on']
        purchased_on = datetime.strptime(purchased_on,  '%Y-%m-%d')
        print(purchased_on)
        person_id = request.POST['person_id']
        print(person_id)
        purchased_by = request.POST['purchased_by']
        date_of_birth = request.POST['date_of_birth']
        if date_of_birth == '':
            date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        gender = request.POST['gender']
        
        start_date = request.POST['start_date']
        if start_date == '':
            start_date = None
        else:
            start_date = datetime.strptime(start_date,  '%Y-%m-%d')
        end_date = request.POST['end_date']  
        if end_date == '':
            end_date = None
        else:
            end_date = datetime.strptime(end_date,  '%Y-%m-%d')
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
       
        if status == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error9': True, 'ani': ani,'date':date})       
        per=User.objects.all() 
        if person_id == "":
             return render(request,'animal_profile/insert_animal_profile.html', {'error7': True, 'per': per,'date':date})    
       
        ins=Animal_profile(
                token_no=token_no,
                name=name,color=color,
                weight=weight,
                category_id=category_id,
                purchase_price=purchase_price,
                purchased_on=purchased_on,
                purchased_by=purchased_by,
                date_of_birth=date_of_birth,
                gender=gender,
                person_id = person_id,
                start_date=start_date,
                end_date=end_date,
                status=status,
                updated_by=1,
                description=description
            )
        ins.save()   
        return redirect(reverse('list_animal_profile'))
    ani=Category.objects.all()
    per=User.objects.all()
    return render(request,'animal_profile/insert_animal_profile.html', {'ani': ani ,'date':date , 'per':per} )
def list_animal_profile(request):
    allTasks = Animal_profile.objects.all()
    return render(request,'animal_profile/list_animal_profile.html', {'animal_pro': allTasks})
# -----------------------------------------------------------------------------------------------------              
# Delete Animal profile
# -----------------------------------------------------------------------------------------------------
def animal_pro_delete(request,animal_id):
    delete = Animal_profile.objects.get(animal_id=animal_id)
    delete.delete()
    return redirect('/list_animal_profile')
# -----------------------------------------------------------------------------------------------------              
# Edit/Update Animal Profile
# -----------------------------------------------------------------------------------------------------
def animal_pro_edit(request , animal_id ):
    animal = Animal_profile.objects.get(animal_id=animal_id)
    ani=Category.objects.all()
    per=User.objects.all()
    return render(request, 'animal_profile/update_animal_profile.html',{'animal':animal,'ani': ani, 'per':per})
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
        category_id=int(category_id)
        status = request.POST['status_val']
        description = request.POST['description']
        person_id = request.POST['person_id']
        person_id=int(person_id)
        print(person_id)
        start_date = request.POST['start_date']
        if start_date == '':
            start_date = None
        else:
            start_date = datetime.strptime(start_date,  '%Y-%m-%d')
        end_date = request.POST['end_date']  
        if end_date == '':
            end_date = None
        else:
            end_date = datetime.strptime(end_date,  '%Y-%m-%d')
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
        if status == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error9': True})       
        else:  
            print(category_id)

            edit = Animal_profile.objects.get(animal_id = animal_id)  

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
            edit.status=status
            edit.description = description 
            edit.person_id = person_id
            edit.person_id = int(person_id)
            edit.start_date=start_date
            edit.end_date=end_date
            edit.updated_on = date    
            edit.save()
            
            return redirect(reverse('list_animal_profile')) 
    animals=Category.objects.all()
    per=User.objects.all()
    return render(request,'animal_profile/update_animal_profile.html', {'animals': animals ,'date':date , 'per':per} )
# -----------------------------------------------------------------------------------------------------              
# Insert Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def insert_pregnancy_detail(request):   
    if request.method == "POST":     
        animal_id = request.POST['animal_id']
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
        pregnant_val = request.POST['pregnant_val']
        is_pregnant = int(pregnant_val)  
        pregnancy_start_date = request.POST['pregnancy_start_date']
        if pregnancy_start_date == '':
            pregnancy_start_date = None
        else:
            pregnancy_start_date = datetime.strptime(pregnancy_start_date,  '%Y-%m-%d')
        pregnancy_end_date = request.POST['pregnancy_end_date']  
        if pregnancy_end_date == '':
            pregnancy_end_date = None
        else:
            pregnancy_end_date = datetime.strptime(pregnancy_end_date,  '%Y-%m-%d')
        description = request.POST['description']        
        det=Animal_profile.objects.all()
        if animal_id == "":
            return render(request,'pregnancy_details/insert_pregnancy_detail.html', {'error2': True , 'det': det,'date':date})
        
        ins=PregnancyDetails(animal_id=animal_id,
        is_pregnancy_confirmed=is_pregnancy_confirmed,
        pregnancy_checked_on=pregnancy_checked_on,
        is_delivery_completed=is_delivery_completed,
        actual_delivery_date=actual_delivery_date,
        is_miscarriage=is_miscarriage,
        miscarriage_date=miscarriage_date,
        infartility=infartility,
        is_pregnant=is_pregnant,
        pregnancy_start_date=pregnancy_start_date,
        pregnancy_end_date=pregnancy_end_date,
        description=description)
        ins.save()   
        return redirect(reverse('list_pregnancy_detail'))
    det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/insert_pregnancy_detail.html', {'det': det ,'date':date } )
# -----------------------------------------------------------------------------------------------------              
# List Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def list_pregnancy_detail(request):
    allTasks = PregnancyDetails.objects.all()
    context = {'animal_det': allTasks}
    return render(request,'pregnancy_details/list_pregnancy_detail.html', context)
# -----------------------------------------------------------------------------------------------------              
# Delete Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def pregnancy_det_delete(request,pregnancy_id):
    delete = PregnancyDetails.objects.get(pregnancy_id=pregnancy_id)
    delete.delete()
    return redirect('/list_pregnancy_detail')
# -----------------------------------------------------------------------------------------------------              
# Edit/Update Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def pregnancy_det_edit(request , pregnancy_id ):
    detail = PregnancyDetails.objects.get(pregnancy_id=pregnancy_id)
    pregnancy_count = PregnancyDetails.objects.filter(is_pregnant = 1).count()
    print(pregnancy_count)
    miscarriage = PregnancyDetails.objects.filter(is_miscarriage = 1).count()
    print(miscarriage)
    is_infartility = PregnancyDetails.objects.filter(infartility = 1).count()
    print(is_infartility)
    det=Animal_profile.objects.all()
    return render(request, 'pregnancy_details/update_pregnancy_detail.html',
                  {'detail':detail,'det': det ,"pregnancy_count":pregnancy_count, 'miscarriage':miscarriage, 'is_infartility':is_infartility})
def update_pregnancy_detail(request, pregnancy_id):
    if request.method == 'POST':
       animal_id = request.POST['animal_id']
      
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
       is_pregnant = request.POST['pregnant_val']
       pregnancy_start_date = request.POST['pregnancy_start_date']
       if pregnancy_start_date == '' or is_pregnant == '0':
            pregnancy_start_date = None
       else:
            pregnancy_start_date = datetime.strptime(pregnancy_start_date,  '%Y-%m-%d')
       pregnancy_end_date = request.POST['pregnancy_end_date']
       if pregnancy_end_date == '' or is_pregnant == '0':
           pregnancy_end_date = None
       else: 
           pregnancy_end_date = datetime.strptime(pregnancy_end_date,  '%Y-%m-%d')
       description = request.POST['description']        
       det=Animal_profile.objects.all()
       if animal_id == "":
           return render(request,'pregnancy_details/update_pregnancy_detail.html', {'error2': True , 'det': det,'date':date})
       else:
           edit = PregnancyDetails.objects.get(pregnancy_id = pregnancy_id)  
           edit.animal_id_id = animal_id      
           edit.is_pregnancy_confirmed = is_pregnancy_confirmed
           edit.pregnancy_checked_on = pregnancy_checked_on
           edit.is_delivery_completed =is_delivery_completed  
           edit.actual_delivery_date=actual_delivery_date        
           edit.is_miscarriage = is_miscarriage
           edit.miscarriage_date = miscarriage_date
           edit.infartility = infartility
           edit.is_pregnant=is_pregnant
           edit.pregnancy_start_date = pregnancy_start_date
           edit.pregnancy_end_date = pregnancy_end_date
           edit.description = description 
           edit.updated_on = date  
           edit.save()         
           return redirect(reverse('list_pregnancy_detail')) 
    det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/update_pregnancy_detail.html', {'det': det ,'date':date } )
# -----------------------------------------------------------------------------------------------------              
# List of Animals
# -----------------------------------------------------------------------------------------------------
def list_of_animals(request):
   # allTasks = Animal_profile.objects.all()
    list_ani = PregnancyDetails.objects.values('infartility','is_miscarriage',
                'is_pregnant','is_pregnancy_confirmed').annotate(count=Count('pregnancy_id'))
    category_counts = Animal_profile.objects.annotate(count=Count('animal_id'))
    result = {}
    for cat in category_counts:
        result[cat.name] = next((item['count'] for item in list_ani if item['is_pregnant'] == cat.name), 0)

    for cat in list_ani:
        infartility = cat['infartility']
        is_miscarriage = cat['is_miscarriage']
        is_pregnant = cat['is_pregnant']
        is_pregnancy_confirmed = cat['is_pregnancy_confirmed']
        animal_count = cat['count']

      
        print(f"infartility: {infartility}, is_miscarriage: {is_miscarriage}, is_pregnant:{is_pregnant},is_pregnancy_confirmed:{is_pregnancy_confirmed}, Count: {animal_count}")
   # combined_queryset = list_ani.union(category_counts)

    # Convert the combined queryset to a list
   # combined_list = list(combined_queryset)

    context = {
        'category_counts': category_counts,
        
    } 
    return render(request,'pregnancy_details/list_of_animals.html', context)
# -----------------------------------------------------------------------------------------------------
# Open User Profile
# -----------------------------------------------------------------------------------------------------
def register_user_profile(request):
    if request.method == 'POST':
        print('came here')
        first_name = request.POST['first_name']
        if first_name == "":
           return render(request,'user_profile/register_user_profile.html', {'error2': True ,'date':date})
        last_name = request.POST['last_name']
        if last_name == "":
           return render(request,'user_profile/register_user_profile.html', {'error3': True ,'date':date})
        username = request.POST['username']
        if username == "":
           return render(request,'user_profile/register_user_profile.html', {'error4': True ,'date':date})
        email = request.POST['email']
        if email == "":
           return render(request,'user_profile/register_user_profile.html', {'error5': True ,'date':date})
        phone_number = request.POST['phone_number']
        # user_group = request.POST['user_group']
        gender = request.POST['gender']
        if gender == "":
           return render(request,'user_profile/register_user_profile.html', {'error8': True ,'date':date})
        city = request.POST['city']
        country = request.POST['country']
        date_of_birth = request.POST['date_of_birth']
        if date_of_birth == '':
           date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        is_active = request.POST['is_active']
        if is_active == "":
           return render(request,'user_profile/register_user_profile.html', {'error9': True ,'date':date})
        user_insert = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            is_active = int(is_active),
            is_superuser = 0,
            is_staff = 0,
            date_joined = date,
            password = 123
        )
        user_insert.save()
        user_profile = UserProfile(
            user_id = user_insert.id,
            phone_number = phone_number,
            gender = gender,
            city = city,
            country = country,
            date_of_birth = date_of_birth
        )
        user_profile.save()

        return  redirect(reverse ('list_user_profile'))  
    user_group = Group.objects.all()
    return render(request,'user_profile/register_user_profile.html',{'user_group':user_group})

def list_user_profile(request):
    user_list = User.objects.all()
    return render(request,'user_profile/list_user_profile.html',{'user_list':user_list})
def delete_user_profile(request,id):
    delete = User.objects.get(id=id)
    delete.delete()
    return redirect('/list_user_profile')
def edit_user_profile(request , id):
    user_profile = User.objects.get(id=id)
    return render(request, 'user_profile/update_user_profile.html',{'user_profile':user_profile})
def update_user_profile(request, id):
    if request.method == 'POST':
       first_name = request.POST['first_name'] 
       if first_name == '':
           first_name = None     
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       phone_number = request.POST['phone_number']
       city = request.POST['city']       
       country = request.POST['country']
       date_of_birth = request.POST['date_of_birth']
       gender = request.POST['gender']
       status = request.POST['status_val']
       description = request.POST['description']
       det=PregnancyDetails.objects.all()
       if first_name == "":
           return render(request,'user_profile/update_user_profile.html', {'error2': True , 'det': det,'date':date})
       else:
           edit = User.objects.get(id = id)  
           edit.first_name = first_name         
           edit.last_name = last_name
           edit.username = username
           edit.email = email  
           edit.phone_number = phone_number        
           edit.city = city
           edit.country = country
           edit.date_of_birth = date_of_birth
           edit.gender=gender
           edit.status = status
           edit.description = description 
           edit.save()         
           return redirect(reverse('list_user_profile')) 
    det=PregnancyDetails.objects.all()
    return render(request,'user_profile/update_user_profile.html', {'det': det ,'date':date } )

# -----------------------------------------------------------------------------------------------------
# Open Groups
# -----------------------------------------------------------------------------------------------------
def insert_group(request):
    if request.method == 'POST':
        print('came here')
        name = request.POST['name']
        if name == "":
           return render(request,'groups/insert_group.html', {'error2': True ,'date':date})       
        user_insert = Group(name = name,)      
        user_insert.save()
        return  redirect(reverse ('list_group'))  
    user_group = Group.objects.all()
    return render(request,'groups/insert_group.html',{'user_group':user_group})

def list_group(request):
    group_list = Group.objects.all()
    return render(request,'groups/list_group.html',{'group_list':group_list})
def delete_group(request,id):
    delete = Group.objects.get(id=id)
    delete.delete()
    return redirect('/list_group')
def edit_group(request , id):
    groups = Group.objects.get(id=id)
    return render(request, 'groups/update_group.html',{'groups':groups})
def update_group(request, id):
    if request.method == 'POST':
       name = request.POST['name'] 
       if name == "":
           return render(request,'groups/update_group.html', {'error2': True ,'date':date})
       else:
           edit = Group.objects.get(id = id)  
           edit.name = name         
           edit.save()         
           return redirect(reverse('list_group')) 
    return render(request,'groups/update_group.html')