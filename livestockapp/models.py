from django.db import models
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
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True)
    purchase_price = models.IntegerField(null=True) 
    purchased_by = models.CharField(blank=True,null=True, max_length=50) 
    purchased_on = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    description= models.TextField(null=True, max_length=50)
    gender = models.CharField(max_length=50,null=True)
    is_pragnent  = models.IntegerField( null=True)
    pragnancy_start_date  = models.DateField(blank=True, null=True)
    pragnancy_end_date  = models.DateField(blank=True, null=True) 
    status =  models.BooleanField(default=True,null=True)
    created_by = models.CharField(max_length=50 ,null=True) 
    created_on  = models.DateField(blank=True, null=True)
    updated_by = models.IntegerField(null=True , blank= True) 
    updated_on = models.DateField(blank=True,null=True)
    def __str__(self):
       return self.animal_id
    
#PregnancyDetails
class PregnancyDetails(models.Model):
    Pregnancy_id = models.AutoField(primary_key=True)  
    start_date = models.DateField(blank=True, null=True) 
    expected_end_date = models.DateField(blank=True, null=True) 
    is_pregnancy_confirmed = models.BooleanField( null=True)
    pregnancy_checked_on = models.DateField(blank=True, null=True) 
    description = models.TextField(blank=True, null=True) 
    is_delivery_completed = models.BooleanField( null=True)
    actual_delivery_date = models.DateField(blank=True, null=True) 
    is_miscarriage = models.BooleanField(blank=True, null=True)
    miscarriage_date = models.DateField(blank=True, null=True) 
    infartility = models.BooleanField(null=True)
    is_pragnent  = models.IntegerField( null=True)
    pragnancy_start_date  = models.DateField(blank=True, null=True)
    pragnancy_end_date  = models.DateField(blank=True, null=True) 
    animal = models.ForeignKey(Animal_profile, null=True, on_delete=models.CASCADE ,related_name="animals_id")
    created_by = models.ForeignKey(Animal_profile, null=True, on_delete=models.CASCADE ,related_name="create_by")
    created_on = models.DateField(blank=True, null=True) 
    updated_by = models.ForeignKey(Animal_profile, null=True, on_delete=models.CASCADE ,related_name="update_by")
    updated_on = models.DateField(blank=True, null=True) 
    def __str__(self):
       return self.description
    