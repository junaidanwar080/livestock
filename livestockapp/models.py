from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50) 
    description= models.TextField(null=True, max_length=50)
    is_active =  models.BooleanField(default=True)
    created_on  = models.DateField(blank=True, null=True)
    updated_on = models.DateField(blank=True, null=True)
    def __str__(self):
       return str(self.category_id)
    
#Animal Profile
class Animal_profile(models.Model):
    animal_id = models.AutoField(primary_key=True)  
    token_no = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True) 
    color = models.CharField(max_length=50,null=True) 
    weight = models.CharField(max_length=50,null=True) 
    category = models.ForeignKey(
                                'Category',
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='animal'
                                    )
    image = models.ImageField(upload_to='images/',null=True)
    purchase_price = models.DecimalField(max_digits=13, decimal_places=2,null=True) 
    ref_party_profile = models.ForeignKey(
                                'RefPartyProfile',
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='animal_pro'
                                    )
    purchased_on = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    description= models.TextField(null=True, max_length=50)
    gender = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(
                                User, 
                                null=True, 
                                on_delete=models.CASCADE,
                                related_name='animal_profile'
                            )
    start_date = models.DateField(blank=True, null=True) 
    end_date = models.DateField(blank=True, null=True) 
    status =  models.BooleanField(default=True,null=True)
    created_by = models.CharField(max_length=50 ,null=True) 
    created_on  = models.DateField(blank=True, null=True)
    updated_by = models.IntegerField(null=True , blank= True) 
    updated_on = models.DateField(blank=True,null=True)
    def str(self): return self.name
    
#PregnancyDetails
class PregnancyDetails(models.Model):
    pregnancy_id = models.AutoField(primary_key=True)  
    is_pregnancy_confirmed = models.BooleanField( null=True)
    pregnancy_checked_on = models.DateField(blank=True, null=True) 
    description = models.TextField(blank=True, null=True) 
    is_delivery_completed = models.BooleanField( null=True)
    actual_delivery_date = models.DateField(blank=True, null=True) 
    is_miscarriage = models.BooleanField(blank=True, null=True)
    miscarriage_date = models.DateField(blank=True, null=True) 
    infartility = models.BooleanField(null=True)
    is_pregnant  = models.IntegerField( null=True)
    pregnancy_start_date  = models.DateField(blank=True, null=True)
    pregnancy_end_date  = models.DateField(blank=True, null=True) 
    animal_profile = models.ForeignKey(
                                'Animal_profile', 
                                null=True, 
                                on_delete=models.CASCADE ,
                                related_name="pregnancy_details"
                                )
    created_by = models.ForeignKey(
                                User, 
                                null=True, 
                                on_delete=models.CASCADE ,
                                related_name="created_pregnancy_details"
                                )
    created_on = models.DateField(blank=True, null=True) 
    updated_by = models.ForeignKey(
                                    User, 
                                    null=True, 
                                    on_delete=models.CASCADE ,
                                    related_name="Updated_pregnancy_details"
                                    )
    updated_on = models.DateField(blank=True, null=True) 
    def __str__(self):
       return self.description


   
    
class UserProfile(models.Model):
    user = models.OneToOneField(
                                User, 
                                on_delete=models.CASCADE
                            )
    phone_number = models.CharField(blank=True,null=True, max_length=30)
    gender = models.TextField(blank=True,null=True, max_length=10) 
    city = models.CharField(blank=True,null=True, max_length=50)
    country = models.CharField(blank=True,null=True, max_length=50) 
    date_of_birth = models.DateField(blank=True,null=True, max_length=50) 
    created_on = models.DateField(blank=True, null=True) 
    updated_on = models.DateField(blank=True, null=True) 
    
#------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# Finance
#--------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
    
# Chart Of Account Model
class ChartOfAccount(models.Model):
    account_no = models.CharField(primary_key=True,max_length = 10)
    main_code = models.CharField(max_length = 10, null=True)
    sub_code = models.CharField(max_length = 10, null=True)
    dept_code = models.CharField(max_length = 10, null=True)
    description = models.CharField(max_length=100, null=True)
    account_type = models.CharField(max_length=100, null=True)
    is_account = models.BooleanField(default=False)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_accounts',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_accounts' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
# Party Type Model
class RefPartyType(models.Model):
    party_type_code = models.CharField(primary_key=True,max_length = 5)
    description = models.CharField(max_length = 200, null=True)
    is_enabled = models.CharField(max_length = 1, null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_party_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_party_type' ,
        null=True,
        on_delete=models.CASCADE,
    )
    

    
# Party Profile Model
class RefPartyProfile(models.Model):
    party_code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    address = models.CharField(max_length = 500, null=True)
    ntn_no = models.CharField(max_length = 50, null=True)
    phone_no = models.CharField(max_length = 50, null=True)
    description = models.CharField(max_length = 500, null=True)
    payment_terms = models.CharField(max_length = 500, null=True)
    ref_party_type = models.ForeignKey(
        'RefPartyType', 
        related_name='party_profile',
        null=True,
        on_delete=models.CASCADE,
    )
    chart_of_account = models.ForeignKey(
        'ChartOfAccount', 
        related_name='ref_party_profile',
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_party_profile',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_party_profile' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
#--------------------------------------------------------------------    
#Vouchers    
#--------------------------------------------------------------------
# Voucher Type
class RefVoucherType(models.Model):
    voucher_type_code = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True)
    is_enabled = models.CharField(max_length=1,null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_voucher_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_voucher_type' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
# Voucher Main
class VoucherMain(models.Model):
    trans_id = models.BigAutoField(primary_key=True)
    voucher_no = models.CharField(max_length=100, null=True)
    voucher_date = models.DateTimeField( null=True)
    ref_voucher_type = models.ForeignKey(
        'RefVoucherType', related_name='voucher_main' ,null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_voucher_main',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_voucher_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
# Voucher Detail
class VoucherDetail(models.Model):
    voucher_main = models.ForeignKey(
        'VoucherMain', 
        related_name='voucher_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    chart_of_account = models.ForeignKey(
        'ChartOfAccount', 
        related_name='voucher_detail' ,
        null=True,max_length=10,
        on_delete=models.CASCADE,
    )
    debit = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    credit = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    description = models.CharField( max_length = 300 ,null=True)
    
# -------------------------------------------------------------------------------
# Stock Management System
# -------------------------------------------------------------------------------
# Stock Type
class StockType(models.Model):
    stock_type_code = models.CharField(primary_key=True , max_length = 20)
    name = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 200, null=True)
    is_enabled = models.CharField(max_length = 1, null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_type' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
#stock in hand
class StockInHand(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 200, null=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    purchase_price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    stock_in_hand = models.CharField(max_length = 18, null=True)
    order_threshold = models.CharField(max_length = 18, null=True)
    stock_type = models.ForeignKey(
        'StockType', 
        related_name='stock_in_hand' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_in_hand',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_in_hand' ,
        null=True,
        on_delete=models.CASCADE,
    )

# --------------------------------------------------------------------------
# Sale
# -------------------------------------------------------------------------
#Stock Sale Main
class StockSaleMain(models.Model):
    invoice_no = models.BigAutoField(primary_key=True)
    invoice_date = models.DateTimeField( null=True)
    ref_party_profile = models.ForeignKey(
        'RefPartyProfile', 
        related_name='stock_sale_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_sale_main',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_sale_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
    
#Stock Sale Details
class StockSaleDetail(models.Model):
    stock_sale_main = models.ForeignKey(
        'StockSaleMain', 
        related_name='sale_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    stock_in_hand = models.ForeignKey(
        'StockInHand', 
        related_name='stock_sale_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=13, decimal_places=3,null=True)

# -------------------------------------------------------------------
# Purchase 
# ------------------------------------------------------------------
# Stock Purchase Main
class StockPurchaseMain(models.Model):
    bill_no = models.CharField(primary_key=True , max_length = 20)
    Bill_date = models.DateTimeField( null=True)
    ref_party_profile = models.ForeignKey(
        'RefPartyProfile', 
        related_name='stock_purchase_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_purchase_main',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_purchase_main' ,
        null=True,
        on_delete=models.CASCADE,
    ) 
    
# Stock Purchase Details
class StockPurchaseDetail(models.Model):
    stock_purchase_main = models.ForeignKey(
        'StockPurchaseMain', 
        related_name='purchase_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    stock_in_hand = models.ForeignKey(
        'StockInHand', 
        related_name='stock_purchase_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    animal_profile = models.ForeignKey(
        'Animal_profile', 
        related_name='animal_purchase_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    


    
    