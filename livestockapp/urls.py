from django.contrib import admin
from django.urls import path
from livestockapp import views
urlpatterns = [
# Home Page Before Login
   path('home', views.home, name='home'),
# Dashboard After Login
   path('dashboard/',views.dashboard, name='dashboard'),
#Category
    path('cat_insert', views.cat_insert, name='insert'),
    path('show/', views.cat_show, name='show' ),
    path('delete/<int:category_id>/', views.cat_delete, name="delete"),
    path('edit/<int:category_id>/', views.cat_edit, name="edit"),
    path('update/<int:category_id>', views.cat_updated, name='update'),
#Animal Profile
    path('insert_animal_profile', views.insert_animal_profile , name='insert_animal_profile'),
    path('list_animal_profile/', views.list_animal_profile, name='list_animal_profile' ),
    path('animal_pro_delete/<int:animal_id>/', views.animal_pro_delete, name="animal_pro_delete"),
    path('animal_pro_edit/<int:animal_id>/', views.animal_pro_edit, name="animal_pro_edit"),
    path('update_animal/<int:animal_id>', views.update_animal, name='update_animal'),
#Pregnancy Details
    path('insert_pregnancy_detail', views.insert_pregnancy_detail , name='insert_pregnancy_detail'),
    path('list_pregnancy_detail/<int:ani_id>', views.list_pregnancy_detail, name='list_pregnancy_detail' ),
    path('pregnancy_det_delete/<int:pregnancy_id>/', views.pregnancy_det_delete, name="pregnancy_det_delete"),
    path('pregnancy_det_edit/<int:pregnancy_id>/', views.pregnancy_det_edit, name="pregnancy_det_edit"),
    path('update_pregnancy_detail/<int:pregnancy_id>', views.update_pregnancy_detail, name='update_pregnancy_detail'),
    path('list_of_animals', views.list_of_animals , name='list_of_animals'),
#Share Animal
    path('shared_animal_payment_input', views.shared_animal_payment_input, name='shared_animal_payment_input'),
    path('shared_animal_person_list/', views.shared_animal_person_list, name='shared_animal_person_list' ),
    path('get_animal_info/<int:animal_id>', views.get_animal_info, name='get_animal_info'),
    
  #  path('edit_animal_profile/<int:animal_id>/', views.edit_animal_profile, name='edit_animal_profile'),

  #  path('shared_animal_payment_update/<int:animal_id>/', views.shared_animal_payment_update, name='shared_animal_payment_update'),
   
# User Profile 
    path('register_user_profile/', views.register_user_profile , name='register_user_profile'),
    path('list_user_profile/', views.list_user_profile, name='list_user_profile' ),
    path('delete_user_profile/<int:id>/', views.delete_user_profile, name="delete_user_profile"),
    path('edit_user_profile/<int:id>/', views.edit_user_profile, name="edit_user_profile"),
    path('update_user_profile/<int:id>', views.update_user_profile, name='update_user_profile'),
    
# Groups
    path('insert_group/', views.insert_group , name='insert_group'),
    path('list_group/', views.list_group, name='list_group' ),
    path('delete_group/<int:id>/', views.delete_group, name="delete_group"),
    path('edit_group/<int:id>/', views.edit_group, name="edit_group"),
    path('update_group/<int:id>', views.update_group, name='update_group'),
    
# User Login 
    path('user_login',views.user_login,name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'), 
    
# ----------------------------------------------------------------------------------------------------------------
# Finance
# ----------------------------------------------------------------------------------------------------------------
# Main page URLs
    # path('',views.main,name='main'),
    
#Chart of Accounts
    #Main Heads
    path('main_head',views.main_head,name='main_head'),
    path('main_head_insert',views.main_head_insert),
    path('main_head_select',views.main_head_select),
    path('main_head_load_for_update/<str:main_code>',views.main_head_load_for_update),
    path('main_head_update',views.main_head_update),
    # Sub Heads
    path('sub_head',views.sub_head,name='sub_head'),
    path('sub_head_insert',views.sub_head_insert ),
    path('sub_head_select',views.sub_head_select),
    path('sub_head_load_for_update/<str:account_code>',views.sub_head_load_for_update),
    path('sub_head_update',views.sub_head_update),
    # Dept Heads
    path('dept_head',views.dept_head,name='dept_head'),
    path('dept_head_insert',views.dept_head_insert ),
    path('dept_head_select',views.dept_head_select),
    path('dept_head_load_for_update/<str:account_code>',views.dept_head_load_for_update),
    path('dept_head_update',views.dept_head_update),
    #Accounts
    path('chart_of_accounts',views.chart_of_accounts,name='chart_of_accounts'),
    path('chart_of_accounts_insert',views.chart_of_accounts_insert),
    path('chart_of_accounts_select',views.chart_of_accounts_select),
    path('chart_of_accounts_load_for_update/<str:account_code>',views.chart_of_accounts_load_for_update),
    path('chart_of_accounts_update',views.chart_of_accounts_update),
    
#Vouchers
    path('journal_voucher',views.journal_voucher,name='journal_voucher'),
    path('all_journal_vouchera',views.all_journal_vouchers,name='all_journal_vouchers'),
    path('voucher_insert',views.voucher_insert),
    path('voucher_detail/<int:Trans_id>',views.voucher_detail),
    
#Voucher Type
    path('voucher_types',views.voucher_types, name='voucher_types'),
    path('voucher_type_insert',views.voucher_type_insert),
    path('select_all_voucher_types',views.select_all_voucher_types),
    path('voucher_type_load_for_update/<int:code>',views.voucher_type_load_for_update),
    path('voucher_type_update',views.voucher_type_update),
     
#Party Type
    path('party_type',views.party_type,name='party_type'),
    path('insert_party_type',views.insert_party_type),
    path('type_select',views.select_party_type),
    path('delete_party_type/<str:party_type_id>',views.delete_party_type),
    path('type_load_for_update/<str:party_type>',views.type_load_for_update , name ='type_load_for_update'),
    path('type_update',views.type_update),
    
#Party Profile
    path('party_profile',views.party_profile,name='party_profile'),
    path('insert_party_profile',views.insert_party_profile),
    path('select_party_profiles',views.select_party_profiles),
    path('party_profile_load_for_update/<int:party_code>',views.party_profile_load_for_update),
    path('update_party_profile',views.update_party_profile),

#Stock
    #stock Type
    # path('stock_type',views.stock_type, name='stock_type'),
    # path('stock_type_select',views.stock_type_select),
    # path('stock_type_insert',views.stock_type_insert),
    # path('stock_type_load_for_update/<str:stock_type_code>',views.stock_type_load_for_update),
    # path('stock_type_update',views.stock_type_update),
    # Finish Goods
    # path('finish_goods',views.finish_goods, name='finish_goods'),
    # path('stock_profile_select',views.stock_profile_select),
    # path('stock_profile_insert',views.stock_profile_insert),
    # Raw Goods
    # path('raw_goods',views.raw_goods, name='raw_goods'),
    # path('raw_goods_select',views.raw_goods_select),
    # path('raw_good_insert',views.raw_good_insert),
# Admin Dashboard
    # path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    


# ------------------------------------------------------------------------------------------------
# Reports
# ------------------------------------------------------------------------------------------------
    path('ledger',views.ledger, name='ledger'),
    path('account_ledger_select',views.account_ledger_select),
    path('get_account_detail',views.get_account_detail),

    
    
#Users
    # path('user_page', views.user_page, name='user_page' ),
    # path('insert_user', views.insert_user),
    # path('select_all_users', views.select_all_users), 
    # path('user_profile_load_for_update/<int:user_id>',views.user_profile_load_for_update),
    # path('update_user_profile',views.update_user_profile),

# Others
    path('load_all_accounts',views.load_all_accounts),
    path('load_all_party_types',views.load_all_party_types),
    # path('party_profiles',views.vendor_profiles),
    # path('load_all_items',views.load_all_items),
    # path('load_item_detail/<int:item_id>',views.load_item_detail),  
    
# ------------------------------------------------------------------------------------------------
# Purchase
# ------------------------------------------------------------------------------------------------
    path('purchase_bill',views.purchase_bill, name='purchase_bill'),
    path('purchase_bill_insert', views.purchase_bill_insert),
    path('bill_details', views.bill_details , name='bill_details'),
    path('edit_bill_details/<str:bill_id>', views.edit_bill_details , name='edit_bill_details'),
    
# ------------------------------------------------------------------------------------------------
# Sale
# ------------------------------------------------------------------------------------------------

    path('sale_invoice',views.sale_invoice,name='sale_invoice'),
    path('sale_invoice_insert', views.sale_invoice_insert),
    path('invoice_details', views.invoice_details , name='invoice_details'),
    
# ------------------------------------------------------------------------------------------------
# Processing
# ------------------------------------------------------------------------------------------------

    # path('processing_voucher',views.processing_voucher, name='processing_voucher'),
    # path('processing_voucher_insert',views.processing_voucher_insert),
    # path('under_process_vouchers',views.under_process_vouchers , name='under_process_vouchers'),
    # path('complete_under_process/<int:processing_id>',views.complete_under_process,name = 'complete_under_process'),
    # path('finish_processing',views.finish_processing,name='finish_processing'),


] 