# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from livestockapp.models import Category, Animal_profile, PregnancyDetails, UserProfile, ShareAnimal
from .models import (
    RefPartyType, 
    ChartOfAccount, 
    VoucherMain, 
    VoucherDetail, 
    RefPartyProfile,
    RefVoucherType,
    StockType,
    StockInHand,
    StockPurchaseMain,
    StockPurchaseDetail,
    StockSaleMain,
    StockSaleDetail,

)
from datetime import datetime
from django.contrib.auth.models import User , Group
from django.db.models import Count,F, Sum ,Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

x = datetime.now() 
date = x.strftime('%Y-%m-%d')


x = datetime.now()
y = x.strftime('%Y-%m-%d')
# -----------------------------------------------------------------------------------------------------
# Home
# -----------------------------------------------------------------------------------------------------
def home(request):
    return render(request,'before_login/home.html')
# -----------------------------------------------------------------------------------------------------
# Dashboard
# -----------------------------------------------------------------------------------------------------
def dashboard(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
        
        return render(request,'dashboard.html',{'user':user,'user_group':user_group})
# -----------------------------------------------------------------------------------------------------
# Catergory Insert
# -----------------------------------------------------------------------------------------------------

def cat_insert(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
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
    return render(request,'animal_category/insert.html',{'user_group':user_group})
# -----------------------------------------------------------------------------------------------------
# List Category 
# -----------------------------------------------------------------------------------------------------
def cat_show(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    allTasks = Category.objects.all()
    context = {'tasks': allTasks,'user_group':user_group}
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
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    cat = Category.objects.get(category_id=category_id)
    return render(request, 'animal_category/update.html',{'cat':cat,'user_group':user_group})
# -----------------------------------------------------------------------------------------------------
# Update Category
# -----------------------------------------------------------------------------------------------------
def cat_updated(request, category_id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
        category_id = request.POST['category_id']
        name = request.POST['name']
        if request.POST.get('name')=="":
            return render(request, 'animal_category/update.html',{'error':True,'user_group':user_group})
        description = request.POST['description']
        if request.POST.get('description')=="":
              return render(request,'animal_category/insert.html', {'error1': True,'user_group':user_group})  
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
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id  
    all_parties = RefPartyProfile.objects.all()
    per=User.objects.all()
   # animal_token=Animal_profile.objects.filter(gender = 'female', status=1).latest('animal_id')
   # animal_token = Animal_profile.objects.filter(gender='female', status=1).order_by('-animal_id').first()


#    if animal_token is None:
   #   latest_token = 1
   # else:
     # latest_token = int(animal_token.token_no) + 1
   
    if request.method == "POST":     
        token_no = request.POST['token_no']
        name = request.POST['ani_name']
        color = request.POST['color']
        category_id = request.POST['category_id']
        weight = request.POST['weight']
        purchase_price = request.POST['purchase_price']
        purchased_on = request.POST['purchased_on']
        purchased_on = datetime.strptime(purchased_on,  '%Y-%m-%d')
        person_id = request.POST['person_id']
        purchased_by = request.POST['purchased_by']
        date_of_birth = request.POST['date_of_birth']
        # voucher_date = request.POST['voucher_date']
        # if voucher_date == '':
        #     voucher_date = None
        # else:
        #     voucher_date = datetime.strptime(voucher_date,  '%Y-%m-%d')
        # print(voucher_date)
        if date_of_birth == '':
            date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        gender = request.POST['gender']
        is_shared = request.POST['is_shared']
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
            return render(request,'animal_profile/insert_animal_profile.html', {'error2': True , 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#'latest_token':latest_token})
        if purchased_by == "":
             return render(request,'animal_profile/insert_animal_profile.html', {'error3': True, 'ani': ani,'date':date,'user_group':user_group,'all_parties':all_parties})    
        # if color == "":
        #     return render(request,'animal_profile/insert_animal_profile.html', {'error4': True, 'ani': ani,'date':date,'user_group':user_group,'all_parties':all_parties})    
        if category_id == "":
             return render(request,'animal_profile/insert_animal_profile.html', {'error5': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token}) 
        if purchase_price == '':
            purchase_price = 0
        if gender == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error6': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token})  
        
        if status == "":
            return render(request,'animal_profile/insert_animal_profile.html', {'error9': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token})       
        per=User.objects.all() 
        if person_id == "":
            # return render(request,'animal_profile/insert_animal_profile.html', {'error7': True, 'per': per,'ani': ani,'date':date,'user_group':user_group,'all_parties':all_parties})    
            person_id == None
            
        try:
            bill_no = StockPurchaseMain.objects.latest('bill_no')
            bill_no = int(bill_no.bill_no) + 1
        except ObjectDoesNotExist:
            bill_no = 1
            
            
        ins=Animal_profile(
                token_no=token_no,
                name=name,color=color,
                weight=weight,
                category_id=category_id,
                purchase_price=purchase_price,
                purchased_on=purchased_on,
                ref_party_profile_id=purchased_by,
                date_of_birth=date_of_birth,
                gender=gender,
                is_shared=is_shared,
                user_id = person_id,
                start_date=start_date,
                end_date=end_date,
                status=status,
                updated_by=1,
                description=description
            )
        ins.save()   
        
        insert_purchase_main=StockPurchaseMain(
                bill_no = bill_no,
                # Bill_date = voucher_date,
                ref_party_profile_id = purchased_by,
                created_on = date,
                created_by_id = user.id
            )
        insert_purchase_main.save()
        insert_purchase_detail=StockPurchaseDetail(
                stock_purchase_main_id = insert_purchase_main.bill_no,
                animal_profile_id  = ins.animal_id,
                quantity = 1,
                price = purchase_price
            )
        insert_purchase_detail.save()
        return redirect(reverse('list_animal_profile'))
    ani_cat=Category.objects.all()
    per=User.objects.all()
    return render(request,'animal_profile/insert_animal_profile.html', {'ani': ani_cat ,'date':date , 'per':per,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token} )
def list_animal_profile(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id 
    allTasks = Animal_profile.objects.all()
    return render(request,'animal_profile/list_animal_profile.html', {'animal_pro': allTasks,'user_group':user_group})
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
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id 
    animal = Animal_profile.objects.get(animal_id=animal_id)
    ani=Category.objects.all()
    per=User.objects.all()
    all_parties = RefPartyProfile.objects.all()
    purchase_detial = ''
    try:
        purchase_detial = StockPurchaseDetail.objects.get(animal_profile_id=animal_id)
    except ObjectDoesNotExist:
        purchase_detial = None
    return render(request, 'animal_profile/update_animal_profile.html',{'animal':animal,'ani': ani, 'per':per,'user_group':user_group,'all_parties':all_parties,'purchase_detial':purchase_detial })

def update_animal(request, animal_id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id 
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
        is_shared = request.POST['is_shared']
        category_id=int(category_id)
        status = request.POST['status_val']
        print(status)
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
        if purchased_by == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error3': True , 'anim': anim,'user_group':user_group})
        if category_id == "":
             return render(request,'animal_profile/update_animal_profile.html', {'error5': True, 'anim': anim,'user_group':user_group})    
        if purchase_price == '':
            purchase_price = 0
        if gender == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error6': True, 'anim': anim,'user_group':user_group})   
        if status == "":
            return render(request,'animal_profile/update_animal_profile.html', {'error9': True, 'anim': anim,'user_group':user_group})       
        
        else:  
            print(category_id)

            edit = Animal_profile.objects.get(animal_id = animal_id)  

            edit.token_no = token_no
            edit.name = name
            edit.color = color
            edit.weight = weight
            edit.category_id =category_id
            edit.purchase_price = float(purchase_price)
            edit.purchased_on = purchased_on
            edit.purchased_by = purchased_by
            edit.date_of_birth = date_of_birth
            edit.gender = gender
            edit.is_shared=is_shared
            edit.status=status 
            print(status)
            edit.description = description 
            edit.user_id = person_id
           # edit.user_id = int(user_id)
            edit.start_date=start_date
            edit.end_date=end_date
            edit.updated_on = date    
            edit.save()
            
            return redirect(reverse('list_animal_profile')) 
    animals=Category.objects.all()
    per=User.objects.all()
    return render(request,'animal_profile/update_animal_profile.html', {'animals': animals ,'date':date , 'per':per,'user_group':user_group} )
# -----------------------------------------------------------------------------------------------------              
# Insert Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def insert_pregnancy_detail(request):   
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    det=Animal_profile.objects.filter(gender = 'female', status=1)
    
    
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
        
        if animal_id == "":
            return render(request,'pregnancy_details/insert_pregnancy_detail.html', {'error2': True , 'det': det,'date':date,'user_group':user_group})
        
        ins=PregnancyDetails(animal_profile_id=animal_id,
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
        return redirect(reverse('list_of_animals'))
    # det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/insert_pregnancy_detail.html', {'det': det ,'date':date ,'user_group':user_group} )
# -----------------------------------------------------------------------------------------------------              
# List Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def list_pregnancy_detail(request,ani_id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    allTasks = PregnancyDetails.objects.filter(animal_profile = ani_id)
    context = {'animal_det': allTasks,'user_group':user_group}
    return render(request,'pregnancy_details/list_pregnancy_detail.html', context)
# -----------------------------------------------------------------------------------------------------              
# Delete Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def pregnancy_det_delete(request,pregnancy_id):
    delete = PregnancyDetails.objects.get(pregnancy_id=pregnancy_id)
    delete.delete()
    return redirect('list_pregnancy_detail')
# -----------------------------------------------------------------------------------------------------              
# Edit/Update Pregnancy Details
# -----------------------------------------------------------------------------------------------------
def pregnancy_det_edit(request , pregnancy_id ):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    detail = PregnancyDetails.objects.get(pregnancy_id=pregnancy_id)
    pregnancy_count = PregnancyDetails.objects.filter(is_pregnant = 1).count()
    print(pregnancy_count)
    miscarriage = PregnancyDetails.objects.filter(is_miscarriage = 1).count()
    print(miscarriage)
    is_infartility = PregnancyDetails.objects.filter(infartility = 1).count()
    print(is_infartility)
    det=Animal_profile.objects.all()
    return render(request, 'pregnancy_details/update_pregnancy_detail.html',
                  {'detail':detail,'det': det ,"pregnancy_count":pregnancy_count, 'miscarriage':miscarriage, 'is_infartility':is_infartility,'user_group':user_group})

def update_pregnancy_detail(request, pregnancy_id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
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
           return render(request,'pregnancy_details/update_pregnancy_detail.html', {'error2': True , 'det': det,'date':date,'user_group':user_group})
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
           return redirect('/list_of_animals')
    det=Animal_profile.objects.all()
    return render(request,'pregnancy_details/update_pregnancy_detail.html', {'det': det ,'date':date ,'user_group':user_group} )
# -----------------------------------------------------------------------------------------------------              
# List of Animals
# -----------------------------------------------------------------------------------------------------
def list_of_animals(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    category_counts = Animal_profile.objects.raw('SELECT ani.animal_id,preg.`pregnancy_id`,preg.`animal_profile_id`, ani.token_no, ani.name, count(is_pregnant) as pregnancy_count, COUNT(CASE WHEN preg.`is_miscarriage` = 1 THEN 1 ELSE NULL END) as Miscarage_count, COUNT(CASE WHEN preg.`infartility` = 1 THEN 1 ELSE NULL END) as Infirtality_count, count(case when (preg.`is_pregnancy_confirmed` =1 AND preg.`is_delivery_completed`=1) THEN 1 ELSE NULL END) as Complete_Deliveries FROM `livestockapp_pregnancydetails` preg join livestockapp_animal_profile ani on ani.animal_id = preg.animal_profile_id WHERE ani.status = 1 group by ani.animal_id')
    
    return render(request,'pregnancy_details/list_of_animals.html', {'category_counts': category_counts,'user_group':user_group})
# -----------------------------------------------------------------------------------------------------
# Open User Profile
# -----------------------------------------------------------------------------------------------------
def register_user_profile(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
        print('came here')
        first_name = request.POST['first_name']
        if first_name == "":
           return render(request,'user_profile/register_user_profile.html', {'error2': True ,'date':date,'user_group':user_group})
        last_name = request.POST['last_name']
        if last_name == "":
           return render(request,'user_profile/register_user_profile.html', {'error3': True ,'date':date,'user_group':user_group})
        username = request.POST['username']
        if username == "":
           return render(request,'user_profile/register_user_profile.html', {'error4': True ,'date':date,'user_group':user_group})
        email = request.POST['email']
        if email == "":
           return render(request,'user_profile/register_user_profile.html', {'error5': True ,'date':date,'user_group':user_group})
        phone_number = request.POST['phone_number']
        # user_group = request.POST['user_group']
        gender = request.POST['gender']
        if gender == "":
           return render(request,'user_profile/register_user_profile.html', {'error8': True ,'date':date,'user_group':user_group})
        city = request.POST['city']
        country = request.POST['country']
        date_of_birth = request.POST['date_of_birth']
        if date_of_birth == '':
           date_of_birth = None
        else:
            date_of_birth = datetime.strptime(date_of_birth,  '%Y-%m-%d')
        is_active = request.POST['is_active']
        if is_active == "":
           return render(request,'user_profile/register_user_profile.html', {'error9': True ,'date':date,'user_group':user_group})
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

        return redirect(reverse ('list_user_profile'))  
    user_group_list = Group.objects.all()
    return render(request,'user_profile/register_user_profile.html',{'user_group_list':user_group_list,'user_group':user_group})

def list_user_profile(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    user_list = User.objects.all()
    return render(request,'user_profile/list_user_profile.html',{'user_list':user_list,'user_group':user_group})
def delete_user_profile(request,id):
    delete = User.objects.get(id=id)
    delete.delete()
    return redirect('/list_user_profile')
def edit_user_profile(request , id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    user_profile = User.objects.get(id=id)
    user_group_list = Group.objects.all()
    return render(request, 'user_profile/update_user_profile.html',{'user_profile':user_profile,'user_group':user_group, 'user_group_list':user_group_list})
def update_user_profile(request, id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
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
           return render(request,'user_profile/update_user_profile.html', {'error2': True , 'det': det,'date':date,'user_group':user_group})
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
    return render(request,'user_profile/update_user_profile.html', {'det': det ,'date':date ,'user_group':user_group} )

# -----------------------------------------------------------------------------------------------------
# Open Groups
# -----------------------------------------------------------------------------------------------------
def insert_group(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
        print('came here')
        name = request.POST['name']
        if name == "":
           return render(request,'groups/insert_group.html', {'error2': True ,'date':date,'user_group':user_group})       
        user_insert = Group(name = name,)      
        user_insert.save()
        return  redirect(reverse ('list_group'))  
    # user_group_list = Group.objects.all()
    return render(request,'groups/insert_group.html',{'user_group':user_group})

def list_group(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    group_list = Group.objects.all()
    return render(request,'groups/list_group.html',{'group_list':group_list,'user_group':user_group})
def delete_group(request,id):
    delete = Group.objects.get(id=id)
    delete.delete()
    return redirect('/list_group')
def edit_group(request , id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    groups = Group.objects.get(id=id)
    return render(request, 'groups/update_group.html',{'groups':groups,'user_group':user_group})
def update_group(request, id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
       name = request.POST['name'] 
       if name == "":
           return render(request,'groups/update_group.html', {'error2': True ,'date':date,'user_group':user_group})
       else:
           edit = Group.objects.get(id = id)  
           edit.name = name         
           edit.save()         
           return redirect(reverse('list_group')) 
    return render(request,'groups/update_group.html',{'user_group':user_group})
# -----------------------------------------------------------------------------------------------------------
# Log In
# -----------------------------------------------------------------------------------------------------------
# User Login
def user_login(request):
    if request.user.id:
        redirect_url = '/dashboard' if request.user.is_superuser else '/home'
        return redirect(redirect_url, permanent=True)
    
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            assert user.check_password(password)
            if user.is_active:
                login(request, user)
                redirect_url = '/dashboard' if user.is_superuser else '/'
                return redirect(redirect_url, permanent=True)
            message = 'Account Temorarily Blocked'
        except (User.DoesNotExist, AssertionError):
            message = "Invaid Credentials"
    return render(request, 'login.html', context={'message': message})
#user_logout 
def user_logout(request):
    logout(request)
    return redirect('home')

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
# Accounts Views
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Chart Of Accounts
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# Main Heads
# ------------------------------------------------------------------------
@login_required(login_url='/home')
def main_head(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    return render(request, 'accounts/chart_of_accounts/main_head/main_head.html', {'user': user,'user_group':user_group})


# Main Head Insert
@login_required(login_url='/home')
def main_head_insert(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
        main_code = request.POST['ac_no']
        ac_name = request.POST['ac_name']

        if main_code == '' or ac_name == '':
            return JsonResponse('Plese Fill Required Fields', safe=False)
        elif (len(main_code) != 2):
            return JsonResponse('Enter 2 digit Main Code', safe=False)
        else:
            ac_code = main_code + '00000000'
            insert_account = ChartOfAccount(account_no=ac_code, 
                                            main_code=main_code, 
                                            description=ac_name,
                                            created_by_id = user.id)
            insert_account.save()
            return JsonResponse("Account Created", safe=False)


# Select Main Head
def main_head_select(request):
    accounts_select = ChartOfAccount.objects.filter(sub_code=None, dept_code=None)
    return render(request, 'accounts/chart_of_accounts/main_head/main_head_select.html',
                  {'accounts_select': accounts_select })


# Main Head load for update
def main_head_load_for_update(request, main_code):
    data = ChartOfAccount.objects.get(account_no=main_code)
    return JsonResponse(model_to_dict(data))


# Main Head update
def main_head_update(request):
    user = request.user
    if request.method == 'POST':
        update_main_code = request.POST['update_ac_no']
        # update_main_code = request.POST['update_main_code']
        update_ac_name = request.POST['update_ac_name']
        if update_main_code == '' or update_ac_name == '':
            return JsonResponse('Please Enter Required fields', safe=False)
        else:
            update = ChartOfAccount.objects.get(account_no=update_main_code)
            update.description = update_ac_name
            update.updated_by_id = user.id
            update.save()
            return JsonResponse('Account Updated', safe=False)


# ------------------------------------------------------------------------
# Sub Heads
# ------------------------------------------------------------------------
@login_required(login_url='/login')
def sub_head(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    main_head = ChartOfAccount.objects.filter(sub_code=None, dept_code=None)
    return render(request, 'accounts/chart_of_accounts/sub_head/sub_head.html',
                  {'main_head': main_head, 'user': user,'user_group':user_group})


# Sub Head Insert
def sub_head_insert(request):
    user = request.user
    if request.method == 'POST':
        sub_code = request.POST['sub_code']
        ac_name = request.POST['ac_name']
        main_code = request.POST['main_code']

        if sub_code == '' or ac_name == '' or main_code == '':
            return JsonResponse('Plese Fill Required Fields', safe=False)
        elif (len(sub_code) != 2):
            return JsonResponse('Enter 2 digit Main Code', safe=False)
        else:
            ac_code = main_code + sub_code + '000000'
            insert_account = ChartOfAccount(account_no=ac_code, main_code=main_code, sub_code=sub_code,
                                              description=ac_name, created_on=y,created_by_id = user.id)
            insert_account.save()
            return JsonResponse("Account Created", safe=False)


# Selecr Main Head
def sub_head_select(request):
    accounts_select = ChartOfAccount.objects.filter(sub_code__isnull=False, dept_code=None)
    return render(request, 'accounts/chart_of_accounts/sub_head/sub_head_select.html',
                  {'accounts_select': accounts_select})


# Sub Head load for update
def sub_head_load_for_update(request, account_code):
    data = ChartOfAccount.objects.get(account_no=account_code)
    return JsonResponse(model_to_dict(data))


# SUb Head update
def sub_head_update(request):
    user = request.user
    if request.method == 'POST':
        update_ac_no = request.POST['edit_ac_no']
        update_main_code = request.POST['edit_main_code']
        update_ac_name = request.POST['edit_ac_name']
        if update_main_code == '' or update_ac_name == '':
            return JsonResponse('Please Enter Required fields', safe=False)
        else:
            update = ChartOfAccount.objects.get(account_no=update_ac_no)
            update.main_code = update_main_code
            update.description = update_ac_name
            update.updated_on = y
            update.updated_by_id = user.id
            update.save()
            return JsonResponse('Account Updated', safe=False)


# ------------------------------------------------------------------------
# Department Heads
# ------------------------------------------------------------------------
@login_required(login_url='/login')
def dept_head(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    main_head = ChartOfAccount.objects.filter(sub_code=None, dept_code=None)
    sub_head = ChartOfAccount.objects.filter(sub_code__isnull=False, dept_code=None)
    return render(request, 'accounts/chart_of_accounts/dept_head/dept_head.html',
                  {'main_head': main_head, 'sub_head': sub_head, 'user': user,'user_group':user_group})


# dept Head Insert
@login_required(login_url='/login')
def dept_head_insert(request):
    user = request.user
    if request.method == 'POST':
        main_code = request.POST['main_code']
        sub_code = request.POST['sub_code']
        dept_code = request.POST['dept_code']
        ac_name = request.POST['ac_name']

        if dept_code == '' or ac_name == '':
            return JsonResponse('Plese Fill Required Fields', safe=False)
        elif (len(dept_code) != 2):
            return JsonResponse('Enter 2 digit Main Code', safe=False)
        else:

            # print(main_code)
            ac_code = main_code + sub_code + dept_code + '0000'
            insert_account = ChartOfAccount(account_no=ac_code, main_code=main_code, sub_code=sub_code,
                                              dept_code=dept_code, description=ac_name, created_on=y, created_by_id = user.id)
            insert_account.save()
            return JsonResponse("Account Created", safe=False)


# Selecr dept Head
@login_required(login_url='/login')
def dept_head_select(request):
    accounts_select = ChartOfAccount.objects.filter(dept_code__isnull=False)
    return render(request, 'accounts/chart_of_accounts/dept_head/dept_head_select.html',
                  {'accounts_select': accounts_select})


# dept Head load for update
@login_required(login_url='/login')
def dept_head_load_for_update(request, account_code):
    data = ChartOfAccount.objects.get(account_no=account_code)
    return JsonResponse(model_to_dict(data))


# dept Head update
def dept_head_update(request):
    user = request.user
    if request.method == 'POST':
        update_ac_no = request.POST['edit_ac_no']
        update_main_code = request.POST['edit_main_code']
        update_sub_code = request.POST['edit_sub_code']

        update_ac_name = request.POST['edit_ac_name']
        if update_main_code == '' or update_ac_name == '':
            return JsonResponse('Please Enter Required fields', safe=False)
        else:
            update = ChartOfAccount.objects.get(account_no=update_ac_no)
            update.main_code = update_main_code
            update.sub_code = update_sub_code
            update.description = update_ac_name
            update.updated_on = y
            update.updated_by_id = user.id
            update.save()
            return JsonResponse('Account Updated', safe=False)


# ------------------------------------------------------------------------
# Accounts
# ------------------------------------------------------------------------
# chart of Accounts page call
@login_required(login_url='/login')
def chart_of_accounts(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    main_head = ChartOfAccount.objects.filter(sub_code=None, dept_code=None)
    sub_head = ChartOfAccount.objects.filter(sub_code__isnull=False, dept_code=None)
    dept_head = ChartOfAccount.objects.filter(dept_code__isnull=False)

    return render(request, 'accounts/chart_of_accounts/accounts/chart_of_accounts.html',
                  {'main_head': main_head, 'sub_head': sub_head, 'dept_head': dept_head, 'user': user,'user_group':user_group})


# Chart of Account Insert
def chart_of_accounts_insert(request):
    user = request.user
    if request.method == 'POST':
        main_code = request.POST['main_code']
        sub_code = request.POST['sub_code']
        dept_code = request.POST['dept_code']
        account_code = request.POST['account_code']
        ac_name = request.POST['ac_name']

        if account_code == '' or ac_name == '':
            return JsonResponse('Plese Fill Required Fields', safe=False)
        elif (len(account_code) != 4):
            return JsonResponse('Enter 4 digit Account Code', safe=False)
        else:
            account_code = main_code + sub_code + dept_code + account_code
            insert_account = ChartOfAccount(
                                                account_no=account_code,
                                                main_code=main_code,
                                                sub_code=sub_code,
                                                dept_code=dept_code,
                                                description=ac_name,
                                                is_account=1,
                                                created_by_id = user.id
                                            )
            insert_account.save()
            return JsonResponse("Account Created", safe=False)


# Selecr Chart of Account

def chart_of_accounts_select(request):
    accounts_select = ChartOfAccount.objects.all()
    # return render(request,'Accounts/chart_of_accounts/Accounts/chart_of_accounts_select.html' , JsonResponse({"accounts_select": accounts_select}))
    return render(request, 'Accounts/chart_of_accounts/Accounts/chart_of_accounts_select.html',
                  {'accounts_select': accounts_select})
    # return JsonResponse({"models_to_return": list(accounts_select)})


# account_load_for_update
def chart_of_accounts_load_for_update(request, account_code):
    data = ChartOfAccount.objects.get(account_no=account_code)
    return JsonResponse(model_to_dict(data))


# chart_of_account_update
def chart_of_accounts_update(request):
    user = request.user
    if request.method == 'POST':
        update_ac_no = request.POST['edit_ac_no']
        update_main_code = request.POST['edit_main_code']
        update_sub_code = request.POST['edit_sub_code']
        edit_dept_code = request.POST['edit_dept_code']
        update_ac_name = request.POST['edit_ac_name']
        if update_main_code == '' or update_ac_name == '':
            return JsonResponse('Please Enter Required fields', safe=False)
        else:
            update = ChartOfAccount.objects.get(account_no=update_ac_no)
            update.main_code = update_main_code
            update.sub_code = update_sub_code
            update.dept_code = edit_dept_code
            update.Account_description = update_ac_name
            update.updated_on = y
            update.updated_by_id = user.id
            update.save()
            return JsonResponse('Account Updated', safe=False)


# ------------------------------------------------------------------------
# Vouchers
# ------------------------------------------------------------------------
# Vouchers
@login_required(login_url='/login')
def all_journal_vouchers(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    select_all = VoucherMain.objects.all()
    return render(request, 'Accounts/Vouchers/journal_vouchers.html', {'select_all': select_all, 'user': user, 'user_group':user_group})


# Voucher Detail
def voucher_detail(request, Trans_id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    voucher_main = VoucherMain.objects.get(trans_id=Trans_id)
    voucher_details = VoucherDetail.objects.filter(voucher_main_id  =Trans_id)
    return render(request, 'accounts/vouchers/voucher_detail.html',
                  {'voucher_main': voucher_main, 'voucher_details': voucher_details,'user_group':user_group})


# Vouchers Input Form
@login_required(login_url='/login')
def journal_voucher(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    all_voucher_types = RefVoucherType.objects.all()
    return render(request, 'Accounts/Vouchers/journal_voucher.html',
                  {'date': y, 'all_voucher_types': all_voucher_types, 'user': user,'user_group':user_group})


# voucher insert
def voucher_insert(request):
    if request.method == 'POST':
        user = request.user
        voucher_no = request.POST['voucher_id']
        voucher_type = request.POST['voucher_type']
        voucher_date = request.POST['voucher_date']
        all_account_codes = request.POST['all_account_codes']
        all_account_codes_list = [x.strip() for x in all_account_codes.split(',')]
        all_debit_accounts = request.POST['all_debit_accounts']
        all_debit_accounts_list = [x.strip() for x in all_debit_accounts.split(',')]
        all_credit_accounts = request.POST['all_credit_accounts']
        all_credit_accounts_list = [x.strip() for x in all_credit_accounts.split(',')]
        all_descriptions = request.POST['all_descriptions']
        all_descriptions_list = [x.strip() for x in all_descriptions.split(',')]
        credit_sum = 0
        debit_sum = 0
        if voucher_no == '' or voucher_type == '':
            return JsonResponse('Please Fill all Required Fields', safe=False)
        else:
            for x in range(len(all_account_codes_list)):
                if all_account_codes_list[x] == '' or all_debit_accounts_list[x] == '' or all_credit_accounts_list[
                    x] == '':
                    return JsonResponse('Please Fill all Required Fields', safe=False)
                else:
                    credit_sum = credit_sum + float(all_credit_accounts_list[x])
                    debit_sum = debit_sum + float(all_debit_accounts_list[x])
            if debit_sum != credit_sum:
                return JsonResponse('Debit And Credit account should be same', safe=False)
            else:
                insert_main = VoucherMain(
                    voucher_no=voucher_no, 
                    ref_voucher_type_id=voucher_type,
                    voucher_date = voucher_date,
                                           created_by_id=user.id)
                insert_main.save()
                for x in range(len(all_account_codes_list)):
                    insert_detail = VoucherDetail(
                        chart_of_account_id=all_account_codes_list[x],
                                                   debit=float(all_debit_accounts_list[x]),
                                                   credit=float(all_credit_accounts_list[x]),
                                                   description=all_descriptions_list[x], 
                                                   voucher_main_id=insert_main.trans_id
                                                   )
                    insert_detail.save()
            return JsonResponse('data inserted successfully', safe=False)
    else:
        return JsonResponse('you have an issue', safe=False)

# ------------------------------------------------------------------------
# Voucher Type
# ------------------------------------------------------------------------
@login_required(login_url='/login')
def voucher_types(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    return render(request, 'Accounts/VoucherType/voucher_types.html', {'user': user,'user_group':user_group})


# select_all_voucher_types
def select_all_voucher_types(request):
    select = RefVoucherType.objects.all()
    return render(request, 'Accounts/VoucherType/voucher_types_select.html', {'select': select})


def voucher_type_insert(request):
    if request.method == 'POST':
        voucher_type_name = request.POST['voucher_type_name']
        if (voucher_type_name == ''):
            return JsonResponse('Please enter Required Data', safe=False)
        else:
            insert_voucher_type = RefVoucherType(description=voucher_type_name, created_on=y)
            insert_voucher_type.save()
            if (insert_voucher_type):
                return JsonResponse('Voucher Type Created', safe=False)
            else:
                return JsonResponse('Voucher Type not Created', safe=False)


# voucher_type_load_for_update
def voucher_type_load_for_update(request, code):
    load_for_update = RefVoucherType.objects.get(voucher_type_code=code)
    return JsonResponse(model_to_dict(load_for_update))


# voucher_type_update
def voucher_type_update(request):
    if request.method == 'POST':
        update_voucher_type_id = request.POST['update_voucher_type_id']
        update_voucher_type_name = request.POST['update_voucher_type_name']
        if update_voucher_type_name == '':
            return JsonResponse('Please Fill Required Fields', safe=False)
        else:
            edit = RefVoucherType.objects.get(voucher_type_code=update_voucher_type_id)
            edit.description = update_voucher_type_name
            edit.updated_on = y
            edit.save()
            return JsonResponse('Voucher Type Updated', safe=False)


# ------------------------------------------------------------------------
# Party Type
# -----------------------------------------------------------------------
@login_required(login_url='/login')
def party_type(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    return render(request, 'Accounts/PartyType/party_type.html', {'user': user,'user_group':user_group})


# insert_party_type
def insert_party_type(request):
    if request.method == "POST":
        party_type_code = request.POST['party_type_code']
        description = request.POST['description']
        is_enable = "1"
        if (party_type_code == '' or description == ''):
            return JsonResponse("Please Fill Required Fields", safe=False)
        else:
            insert_type = RefPartyType(party_type_code=party_type_code, description=description, is_enabled=is_enable,
                                         created_on=y)
            insert_type.save()
            return JsonResponse('data inserted', safe=False)


# select_party_type
def select_party_type(request):
    type_select = RefPartyType.objects.all()
    return render(request, 'Accounts/PartyType/party_type_select.html', {'type_select': type_select})


# delete_party_type
def delete_party_type(request, party_type_id):
    delete_party_type = RefPartyType.objects.get(party_type_code=party_type_id)
    msg = delete_party_type.delete()
    if (msg):
        return redirect('party_type')
    else:
        return JsonResponse('data not deleted', safe=False)


# Type Load For Update
def type_load_for_update(request, party_type):
    print(party_type)
    type = RefPartyType.objects.get(party_type_code=party_type)
    return JsonResponse(model_to_dict(type))


# type Update
def type_update(request):
    if request.method == 'POST':
        if (request.POST['update_description'] == ''):
            return JsonResponse('Please write name', safe=False)
        else:
            party_type_code = request.POST['update_party_type_code']
            description = request.POST['update_description']
            update_on = y
            type_data = RefPartyType.objects.get(party_type_code=party_type_code)
            type_data.description = description
            type_data.updated_on = update_on
            type_data.save()
            return JsonResponse('Type Record Updated', safe=False)


# ---------------------------------------------------------------------------------------------------------
# party_Profile
# ---------------------------------------------------------------------------------------------------------
@login_required(login_url='/login')
def party_profile(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    return render(request, 'accounts/Party_Profile/party_profile.html', {'user': user, 'user_group':user_group})


def select_party_profiles(request):
    select_all = RefPartyProfile.objects.all()
    return render(request, 'accounts/party_profile/party_profiles_select.html', {'select_all': select_all})


# insert Party Profile
def insert_party_profile(request):
    if request.method == 'POST':
        party_name = request.POST['party_name']
        account = request.POST['account']
        ntn_number = request.POST['ntn_number']
        address = request.POST['address']
        phone_no = request.POST['phone_no']
        description = request.POST['description']
        party_type_code = request.POST['party_type_code']
        if (party_name == '' or ntn_number == '' or account == ''):
            return JsonResponse('Please Fill Required Fields', safe=False)
        else:
            print('Account id: ',account)
            print('party_type_code : ',party_type_code)
            party_profile_insert = RefPartyProfile(
                                                    name=party_name, 
                                                    address=address, 
                                                    ntn_no=ntn_number,
                                                    phone_no=phone_no,
                                                    description=description, 
                                                    ref_party_type_id=party_type_code,
                                                    chart_of_account_id=account,
                                                    
                                                )
            party_profile_insert.save()
            return JsonResponse('data inserted', safe=False)
    else:
        return JsonResponse('You are sending Wrong Request', safe=False)


# party_profile_load_for_update
def party_profile_load_for_update(request, party_code):
    party_profile_load = RefPartyProfile.objects.get(party_code=party_code)
    return JsonResponse(model_to_dict(party_profile_load))


# update_party_profile
def update_party_profile(request):
    if request.method == 'POST':
        update_party_code = request.POST['update_party_code']
        update_party_name = request.POST['update_party_name']
        update_account = request.POST['update_account']
        update_ntn_number = request.POST['update_ntn_number']
        update_address = request.POST['update_address']
        update_phone_no = request.POST['update_phone_no']
        update_description = request.POST['update_description']
        data = RefPartyProfile.objects.get(party_code=update_party_code)
        data.name = update_party_name
        data.chart_of_account_id = update_account
        data.ntn_no = update_ntn_number
        data.address = update_address
        data.phone_no = update_phone_no
        data.description = update_description
        data.save()
        return JsonResponse('Party Record Updated', safe=False)


# --------------------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def user_page(request):
#     username = request.user.username
#     return render(request, 'Admin_Penal/User/users.html', {'username': username})


# Insert User
# def insert_user(request):
#     if request.method == "POST":
#         # User_id = request.POST['User_id']
#         Name = request.POST['Name']
#         Email = request.POST['Email']
#         # Phone = request.POST['Phone']
#         # Gender = request.POST['Gender']
#         Login_Name = request.POST['Login_Name']
#         Password = request.POST['Password']
#         # Company_Cde_id = request.POST['Company_Cde_id']
#         # print( Name, Email, Phone, Gender, Login_Name, Password, Company_Cde_id)
#         super_admin = 1
#         ins = User.objects.create_user(first_name=Name, email=Email, username=Login_Name, password=Password,
#                                        is_superuser=super_admin)
#         ins.save()
#         send_mail(
#             'Test Mail',
#             'It is testing email',
#             'junaidanwar080@gmail.com',
#             [Email],
#         )
#         return JsonResponse('User Created', safe=False)


# Select User
# def select_all_users(request):
#     allusers = User.objects.all()
#     return render(request, 'Admin_Penal/User/select_all_users.html', {'User_table': allusers})


# def user_profile_load_for_update(request, user_id):
#     # print('came here')
#     user_data = User.objects.get(id=user_id)
#     return JsonResponse(model_to_dict(user_data))


# def update_user_profile(request):
#     if request.method == "POST":
#         edit_user_id = request.POST['edit_user_id']
#         edit_first_name = request.POST['edit_first_name']
#         edit_last_name = request.POST['edit_last_name']
#         edit_user_name = request.POST['edit_username']
#         user_id = User.objects.get(id=edit_user_id)
#         user_id.username = edit_user_name
#         user_id.first_name = edit_first_name
#         user_id.last_name = edit_last_name
#         user_id.save()
#         return JsonResponse("User Data Updated", safe=False)


# -------------------------------------------------------------------------------
# Stock
# -------------------------------------------------------------------------------
# Stock Type
# -------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def stock_type(request):
#     user= request.user
#     return render(request, 'accounts/stock/stock_type/Stock_type.html', {'username': user})


# # select Stock Stype
# def stock_type_select(request):
#     stock = StockType.objects.all()
#     return render(request, 'accounts/stock/stock_type/stock_type_select.html', {'stock': stock})


# # insert Stock Type
# def stock_type_insert(request):
#     user= request.user
#     if request.method == 'POST':
#         stock_type_code = request.POST['stock_type_code']
#         name = request.POST['name']
#         description = request.POST['description']
#         if (stock_type_code == '' or name == ''):
#             return JsonResponse('Please Fill Required Fields', safe=False)
#         else:
#             Stock_type_insert = StockType(stock_type_code=stock_type_code, name=name, description=description,
#                                            created_on=y,created_by_id=user.id)
#             Stock_type_insert.save()
#             return JsonResponse('Stock Type Created', safe=False)
#     else:
#         return JsonResponse('You are sending Wrong Request', safe=False)


# # Stock type data Load for Update
# def stock_type_load_for_update(request, stock_type_code):
#     party_profile_load = StockType.objects.get(stock_type_code=stock_type_code)
#     return JsonResponse(model_to_dict(party_profile_load))


# # Stock type Update
# def stock_type_update(request):
#     user= request.user
#     if request.method == 'POST':
#         edit_stock_type_code = request.POST['edit_stock_type_code']
#         edit_name = request.POST['edit_name']
#         edit_description = request.POST['edit_description']
#         if (edit_stock_type_code == '' or edit_name == ''):
#             return JsonResponse('Please Fill Required Fields', safe=False)
#         else:
#             data = StockType.objects.get(stock_type_code=edit_stock_type_code)
#             data.stock_type_code = edit_stock_type_code
#             data.name = edit_name
#             data.description = edit_description
#             data.updated_on = y
#             data.updated_by_id = user.id
#             data.save()
#             return JsonResponse('Stock Type Updated', safe=False)


# # -------------------------------------------------------------------------------
# # Stock Profile (Finish Goods)
# # -------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def finish_goods(request):
#     user= request.user
#     select_stock_type = StockType.objects.all()
#     return render(request, 'accounts/stock/stock_profile/stock_profile.html',
#                   {'username': user, 'select_stock_type': select_stock_type})

# # Stock Profile Select
# def stock_profile_select(request):
#     stock = StockInHand.objects.filter(stock_type_id=1234)
#     if stock.exists():
#         # stock = StockInHand.objects.filter(stock_type_id=123)
#         print('records found')
#     else:
#         print('No records found')
#         messages.error(request, 'No Resord found')
#     return render(request, 'accounts/stock/stock_profile/stock_profile_select.html', {'stock': stock})

# # Stock Profile insert
# def stock_profile_insert(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         sale_price = request.POST['sale_price']
#         if (sale_price == ''):
#             sale_price = 0.00
#         purchase_price = request.POST['purchase_price']
#         if (purchase_price == ''):
#             purchase_price = 0.00
#         description = request.POST['description']
#         stock_type_id = request.POST['stock_type_id']
#         if (name == ''):
#             return JsonResponse('Please Fill Required Fields', safe=False)
#         else:
#             stock_type_insert = StockInHand(name=name, description=description, sale_price=sale_price,
#                                               purchase_price=purchase_price, stock_type_id=stock_type_id,
#                                               created_on=y)
#             stock_type_insert.save()
#             return JsonResponse('New Item Added', safe=False)
#     else:
#         return JsonResponse('You are sending Wrong Request', safe=False)
    
# -------------------------------------------------------------------------------
# Stock Profile (Raw Goods)
# -------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def raw_goods(request):
#     user= request.user
#     select_stock_type = StockType.objects.all()
#     return render(request, 'accounts/stock/stock_profile/raw_goods/raw_good_profile.html',{'username': user , 'select_stock_type':select_stock_type})

# # Stock Profile Select
# def raw_goods_select(request):
#     stock = StockInHand.objects.filter(stock_type_id=123)
#     if stock.exists():
#         # stock = StockInHand.objects.filter(stock_type_id=123)
#         print('records found')
#     else:
#         print('No records found')
#         messages.error(request, 'No Resord found')
#     return render(request, 'accounts/stock/stock_profile/raw_goods/raw_good_select.html', {'stock': stock})

# # Stock Profile insert
# def raw_good_insert(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         sale_price = request.POST['sale_price']
#         if (sale_price == ''):
#             sale_price = 0.00
#         purchase_price = request.POST['purchase_price']
#         if (purchase_price == ''):
#             purchase_price = 0.00
#         description = request.POST['description']
#         stock_type_id = request.POST['stock_type_id']
#         if (name == ''):
#             return JsonResponse('Please Fill Required Fields', safe=False)
#         else:
#             stock_type_insert = StockInHand(name=name, description=description, sale_price=sale_price,
#                                               purchase_price=purchase_price, stock_type_id=stock_type_id,
#                                               created_on=y)
#             stock_type_insert.save()
#             return JsonResponse('New Item Added', safe=False)
#     else:
#         return JsonResponse('You are sending Wrong Request', safe=False)


# -------------------------------------------------------------------------------
# Log in , Logout
# -------------------------------------------------------------------------------


# insert login
# def insert_login(request):
#     if request.user.id:
#         redirect_url = '/admin_dashboard' if request.user.is_superuser else '/'
#         return redirect(redirect_url, permanent=True)

#     message = ''
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         # user = authenticate( username=username, password=password)
#         try:
#             user = User.objects.get(username=username)
#             assert user.check_password(password)
#             if user.is_active:
#                 login(request, user)
#                 redirect_url = '/admin_dashboard' if user.is_superuser else '/'
#                 return redirect(redirect_url, permanent=True)
#             message = 'Account Temorarily Blocked'
#         except (User.DoesNotExist, AssertionError):
#             message = "Invaid Credentials"
#     return render(request, 'login.html', context={'message': message})


# logout
# def logout_user(request):
#     logout(request)
#     # request.session.flush()
#     # request.session.clear_expired()
#     return redirect('/login', permanent=True)


# ---------------------------------------------------------------------------------
# Admin Dash Board
# ---------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def admin_dashboard(request):
#     username = request.user.username
#     return render(request, 'Admin_Penal/Admin_Dashboard.html', {'username': username})



# -------------------------------------------------------------------------------
# Reports
# -------------------------------------------------------------------------------
# Ledger
# -------------------------------------------------------------------------------
@login_required(login_url='/login')
def ledger(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    return render(request, 'accounts/reports/ledger/account_ledger.html', {'user': user , 'date':y,'user_group':user_group})


def account_ledger_select(request):
    # ledger = Voucher_detail.objects.all()
    ledger = VoucherDetail.objects.values('chart_of_account_id','chart_of_account__description', 'description', 'debit','credit','voucher_main__created_on')
    ledger_list = list(ledger)
    previous_balance = 0
    for entry in ledger_list:
        entry['balance'] = previous_balance + entry['debit'] - entry['credit']
        previous_balance = entry['balance']
        
    return render(request, 'accounts/reports/ledger/account_ledger_select.html', {'ledger': ledger_list})
def get_account_detail(request):
    if request.POST:
        to_date_str = request.POST['to_date']
        from_date_str = request.POST['from_date']
        to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()
        from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
        account_no = request.POST['account_no']
        ledger = VoucherDetail.objects.filter( 
            chart_of_account_id = account_no,
            voucher_main__voucher_date__range=[from_date,to_date]
        ).values('chart_of_account_id','chart_of_account__description', 'description', 'debit','credit','voucher_main__created_on')
        
        # Convert to a list of dictionaries
        ledger_list = list(ledger)
        
        # Calculate balance for each entry
        previous_balance = 0
        for entry in ledger_list:
            entry['balance'] = previous_balance + entry['debit'] - entry['credit']
            previous_balance = entry['balance']
            print(previous_balance)
        return render(request, 'accounts/reports/ledger/account_ledger_select.html', {'ledger': ledger_list})


# -------------------------------------------------------------------------------
# Others
# -------------------------------------------------------------------------------
def load_all_accounts(request):
    select_accounts = ChartOfAccount.objects.filter(is_account = 1)
    return render(request, 'accounts/other/load_all_accounts.html', {'select_accounts': select_accounts})


def load_all_party_types(request):
    all_types = RefPartyType.objects.all()
    return render(request, 'accounts/other/load_all_party_types.html', {'all_types': all_types})


def vendor_profiles(request):
    vender_list = RefPartyProfile.objects.filter(ref_party_type_id=1234)
    return render(request, 'Accounts/other/vendor_profiles.html', {'vender_list': vender_list})

# def load_all_items(request):
#     item_list = StockInHand.objects.all()
#     return render(request, 'Accounts/other/item_name_load.html', {'item_list': item_list})

# def load_item_detail(request, item_id):
#     item_detail = StockInHand.objects.get(stock_id=item_id)
#     return JsonResponse(model_to_dict(item_detail))

# -------------------------------------------------------------------------------
# Purchase Bill
# -------------------------------------------------------------------------------
# @login_required(login_url='/login')
def purchase_bill(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    vender_list = RefPartyProfile.objects.filter(ref_party_type_id=1234)
    return render(request, 'Accounts/Purchase/purchase_bill.html', {'user': user, 'date': y , 'vender_list':vender_list,'user_group':user_group})


def purchase_bill_insert(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    if request.method == 'POST':
        user = request.user
        bill_id = request.POST['bill_id']
        vendor_id = request.POST['vendor_id']
        posted_date = request.POST['Posted_date']
        all_item_code = request.POST['all_item_code']
        all_item_code_list = [x.strip() for x in all_item_code.split(',')]
        all_item_quantity = request.POST['all_item_quantity']
        all_item_quantity_list = [x.strip() for x in all_item_quantity.split(',')]
        all_unit_price = request.POST['all_unit_price']
        all_unit_price_list = [x.strip() for x in all_unit_price.split(',')]
        if vendor_id=='' or posted_date=='' or bill_id=="":
            return JsonResponse('Please Fill all Required Fields', safe=False)
        else:
            for x in range(len(all_item_code_list)):
                if all_item_code_list[x] == '' or all_item_quantity_list[x] == '' or all_unit_price_list[x] == '':
                    return JsonResponse('Please Fill all Required Fields', safe=False)
            insert_main = StockPurchaseMain(
                bill_no=bill_id,
                ref_party_profile_id=vendor_id,
                Bill_date=posted_date,
                created_by_id=user.id
            )
            insert_main.save()
            # last_bill_date = Stock_purchase_main.objects.aggregate(max_bill_date=Max('created_on'))
            # last_bill = Stock_purchase_main.objects.get(created_on=last_bill_date['max_bill_date'])
            # print('Last Inserted1: ', type(last_bill.Bill_No))
            # print('Last Inserted1: ', type(bill_id))
            for x in range(len(all_item_code_list)):
                curent_stock = StockInHand.objects.get(stock_id=all_item_code_list[x])
                if curent_stock.stock_in_hand is None:
                    curent_stock.stock_in_hand = 0
                update_inventory = int(curent_stock.stock_in_hand) + int(all_item_quantity_list[x])
                update_stock = StockInHand.objects.get(stock_id=all_item_code_list[x])
                update_stock.stock_in_hand = update_inventory
                update_stock.save()
                insert_detail = StockPurchaseDetail(
                    stock_in_hand_id=all_item_code_list[x],
                    quantity=all_item_quantity_list[x],
                    price=float(all_unit_price_list[x]),
                    stock_purchase_main_id=bill_id
                )
                insert_detail.save()
            return JsonResponse('Data Inserted', safe=False)
       


# Bill Details
def bill_details(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    select_details = StockPurchaseDetail.objects.values(
            'stock_purchase_main__bill_no', 
            'stock_purchase_main__created_by__username',
            'stock_purchase_main__created_on',
            'stock_purchase_main__ref_party_profile__name',
            'stock_purchase_main__Bill_date'
        
        ).annotate(
                    res_price=Sum('price')
                    )
    sum_res_price = select_details.aggregate(total_res_price = Sum('res_price'))
    total_res_price = sum_res_price['total_res_price']
    count_bills = StockPurchaseMain.objects.count()
    return render(request, 'accounts/purchase/bill_details.html', {'select_details': select_details , 'total_res_price':total_res_price , 'count_bills':count_bills,'user_group':user_group})


# Edit purchase bill_details
def edit_bill_details(request, bill_id):
    user = request.user
    total_prices = []
    select_main = StockPurchaseMain.objects.get(bill_no=bill_id)
    select_details = StockPurchaseDetail.objects.filter(stock_purchase_main_id=bill_id)
    for i in select_details:
        i.total_price = i.quantity * i.price
        total_prices.append(i.total_price)
    total_price_sum = sum(total_prices)
    print(select_main.created_on)
    return render(request, 'accounts/purchase/purchase_detail/purchase_detail.html',
                  {'select_details': select_details, 'select_main': select_main, 'total_price_sum': total_price_sum,
                   'user': user})


# -------------------------------------------------------------------------------
# Sale Invoice
# -------------------------------------------------------------------------------
@login_required(login_url='/login')
def sale_invoice(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    customer_list = RefPartyProfile.objects.filter(ref_party_type_id=123)
    return render(request, 'accounts/sale/sale_invoice.html', {'username': user, 'date': y , 'customer_list':customer_list,'user_group':user_group})


# Sale Invoice Insert
def sale_invoice_insert(request):
    if request.method == 'POST':
        user = request.user
        invoice_id = request.POST['bill_id']
        customer_id = request.POST['vendor_id']
        invoice_date = request.POST['Posted_date']
        all_item_code = request.POST['all_item_code']
        all_item_code_list = [x.strip() for x in all_item_code.split(',')]
        all_item_quantity = request.POST['all_item_quantity']
        all_item_quantity_list = [x.strip() for x in all_item_quantity.split(',')]
        all_unit_price = request.POST['all_unit_price']
        all_unit_price_list = [x.strip() for x in all_unit_price.split(',')]
        if customer_id == '' or invoice_date == '' or invoice_id == '':
            return JsonResponse('Please Fill all Required Fields', safe=False)
        else:
            for x in range(len(all_item_code_list)):
                if all_item_code_list[x] == '' or all_item_quantity_list[x] == '' or all_unit_price_list[x] == '':
                    return JsonResponse('Please Fill all Required Fields', safe=False)

            insert_main = StockSaleMain(
                            invoice_no=invoice_id, 
                            ref_party_profile_id=customer_id,
                            invoice_date =invoice_date,
                            created_by_id = user.id
                            )
            insert_main.save()
            # invoice_id = StockSaleMain.objects.latest('Invoice_No')
            for x in range(len(all_item_code_list)):
                curent_stock = StockInHand.objects.get(stock_id=all_item_code_list[x])
                if curent_stock.stock_in_hand is None:
                    curent_stock.stock_in_hand = 0
                update_inventory = int(curent_stock.stock_in_hand) - int(all_item_quantity_list[x])
                update_stock = StockInHand.objects.get(stock_id=all_item_code_list[x])
                update_stock.stock_in_hand = update_inventory
                update_stock.save()
                insert_detail = StockSaleDetail(
                                                stock_in_hand_id=all_item_code_list[x], 
                                                quantity=all_item_quantity_list[x],
                                                price=float(all_unit_price_list[x]), 
                                                stock_sale_main_id=insert_main.invoice_no
                                                  )
                insert_detail.save()
            return JsonResponse('Data Inserted', safe=False)


# Invoice Details
def invoice_details(request):
    # select_details = Stock_purchase_detail.objects.all().select_related('Bill_no')
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id
    select_details = StockSaleDetail.objects.values(
                                                    'stock_sale_main',
                                                    'stock_sale_main__invoice_no',
                                                    'stock_sale_main__ref_party_profile__name',
                                                    'stock_sale_main__created_on'
                                                ).annotate(
                                                    res_price=Sum('price')
                                                )
    sum_res_price = select_details.aggregate(total_res_price = Sum('res_price'))
    total_res_price = sum_res_price['total_res_price']
    count_invoice = StockSaleMain.objects.count()
    return render(request, 'accounts/Sale/invoice_details.html', {'select_details': select_details , 'count_invoice':count_invoice , 'total_res_price':total_res_price ,'user_group':user_group})




# -----------------------------------------------------------------------------------------------------              
# Insert Animal Profile
# -----------------------------------------------------------------------------------------------------
def shared_animal_payment_input(request): 
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id  
    all_parties = RefPartyProfile.objects.all()
    per=User.objects.all()
    det=Animal_profile.objects.all()
    
    if request.method == "POST":     
        token_no = request.POST['token_no']
        #print(token_no)
        name = request.POST['ani_name']
        color = request.POST['color']
        category_id = request.POST.get('category_id')
        weight = request.POST['weight']
        person_id = request.POST.get('person_id')
        gender = request.POST.get('gender')
        payment = request.POST['payment']
        month = request.POST['month']
        start_date = request.POST['start_date']
        if start_date == '':
            start_date = None
        #else:
          #  start_date = datetime.strptime(start_date,  '%Y-%m-%d')
        end_date = request.POST['end_date']  
        if end_date == '':
            end_date = None
       # else:
          #  end_date = datetime.strptime(end_date,  '%Y-%m-%d')
        status = request.POST['status_val']
        description = request.POST['description']        
        ani=Category.objects.all()
        if token_no == "":
            return render(request,'share_animal/shared_animal_payment_input.html', {'error2': True , 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#'latest_token':latest_token})
        # if color == "":
        #     return render(request,'share_animal/shared_animal_payment_input.html', {'error4': True, 'ani': ani,'date':date,'user_group':user_group,'all_parties':all_parties})    
        #if category_id == "":
            # return render(request,'share_animal/shared_animal_payment_input.html', {'error5': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token}) 
       
       # if gender == "":
           # return render(request,'share_animal/shared_animal_payment_input.html', {'error6': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token})  
        
        if status == "":
            return render(request,'share_animal/shared_animal_payment_input.html', {'error9': True, 'ani': ani,'per':per,'date':date,'user_group':user_group,'all_parties':all_parties})#,'latest_token':latest_token})       
        per=User.objects.all() 
        if person_id == "":
            # return render(request,'share_animal/shared_animal_payment_input.html', {'error7': True, 'per': per,'ani': ani,'date':date,'user_group':user_group,'all_parties':all_parties})    
            person_id == None
            
        ins=Animal_profile(
                token_no=token_no,

                name=name,color=color,
                weight=weight,
                category_id=category_id,
                gender=gender,
                user_id = person_id,
                status=status,
                description=description,
                start_date = start_date,
                end_date = end_date
            ) 
        ins.save() 
        instanse = ShareAnimal(
            payment=payment,
            month = month,
            
        )  
        instanse.save()
        return redirect(reverse('shared_animal_person_list'))
    ani_share=Category.objects.all()    
    per=User.objects.all()
    return render(request,'share_animal/shared_animal_payment_input.html', {'ani': ani_share ,'date':date , 'per':per,'user_group':user_group,'all_parties':all_parties , 'det':det})#,'latest_token':latest_token} )

def get_animal_info(request, animal_id):
    animal_data = Animal_profile.objects.get(animal_id=animal_id)
    if animal_data:
        data = {
            #'animal_id': animal_data.animal_id,
            'token_no': animal_data.token_no,
            'ani_name': animal_data.name,
            'color': animal_data.color,
            'weight': animal_data.weight,
            'category_id': animal_data.category_id,
            'gender': animal_data.gender,
            'user_id': animal_data.user_id,
            'start_date': animal_data.start_date,
            'end_date': animal_data.end_date,
            'status': animal_data.status,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Animal not found'}, status=404)

def shared_animal_person_list(request):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id 

    # Annotate the number of animals each user owns
    party_profiles = RefPartyProfile.objects.annotate(number_of_animals=Count('animal_pro'))
    print(party_profiles)
    det = Animal_profile.objects.all()
    return render(request, 'share_animal/shared_animal_person_list.html', {'party_profiles': party_profiles, 'user_group': user_group, 'det': det})









def edit_animal_profile(request , animal_id):
    print("sdddd")
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id 
    party_profile = Animal_profile.objects.get(id=animal_id)
    ani=Category.objects.all()
    per=User.objects.all()
    all_parties = RefPartyProfile.objects.all()
    share = ShareAnimal.objects.all()
    return render(request, 'share_animal/shared_animal_payment_update.html',{'party_profile':party_profile,'ani': ani, 'per':per,'user_group':user_group,'all_parties':all_parties,'share':share })

def shared_animal_payment_update(request,id):
    user = request.user
    if user.is_authenticated and user.groups.exists():
        user_group = user.groups.first().id  
    all_parties = RefPartyProfile.objects.all()
    per=User.objects.all()
    det=Animal_profile.objects.all()
    
    if request.method == "POST":     
        token_no = request.POST['token_no']
        #print(token_no)
        name = request.POST['ani_name']
        color = request.POST['color']
        category_id = request.POST['category_id']
        weight = request.POST['weight']
        person_id = request.POST['person_id']
        gender = request.POST['gender']
        payment = request.POST['payment']
        month = request.POST['month']
        start_date = request.POST['start_date']
        if start_date == '':
            start_date = None
        #else:
          #  start_date = datetime.strptime(start_date,  '%Y-%m-%d')
        end_date = request.POST['end_date']  
        if end_date == '':
            end_date = None
       # else:
          #  end_date = datetime.strptime(end_date,  '%Y-%m-%d')
        status = request.POST['status_val']
        description = request.POST['description']   
        anim=Category.objects.all()     
        if status == "":
            return render(request,'share_animal/shared_animal_payment_update.html', {'error9': True, 'anim': anim,'user_group':user_group})       
        
        else:  
            print(category_id)

            edit = Animal_profile.objects.get(animal_id = id)  

            edit.token_no = token_no
            edit.name = name
            edit.color = color
            edit.weight = weight
            edit.category_id =category_id
           
            edit.payment = payment
            edit.gender = gender
            edit.month=month
            edit.status=status 
            print(status)
            edit.description = description 
            edit.user_id = person_id
           # edit.user_id = int(user_id)
            edit.start_date=start_date
            edit.end_date=end_date
            edit.updated_on = date    
            edit.save()
            
            return redirect(reverse('shared_animal_person_list')) 
    animals=Category.objects.all()
    per=User.objects.all()
    return render(request,'share_animal/shared_animal_payment_update.html', {'animals': animals ,'date':date , 'per':per,'user_group':user_group} )

