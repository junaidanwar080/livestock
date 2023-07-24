from django.db import models
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50) 
    description= models.TextField(null=True, max_length=50)
    is_active =  models.BooleanField(default=True)
    created_on  = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    def __str__(self):
       return self.category_id
    
#Animal Profile
class Animal_profile(models.Model):
    id = models.AutoField(primary_key=True)  
    token_no = models.IntegerField(max_length=50)
    name = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 
    weight = models.CharField(max_length=50) 
    category_id = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    purchase_price = models.IntegerField(max_length=50) 
    purchased_by = models.IntegerField(max_length=50) 
    purchased_on = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    description= models.TextField(null=True, max_length=50)
    gender = models.CharField(max_length=50)
    is_pragnent  = models.IntegerField(blank=True, null=True)
    pragnancy_start_date  = models.DateTimeField(blank=True, null=True)
    pragnancy_end_date  = models.DateTimeField(blank=True, null=True) 
    status =  models.BooleanField(default=True)
    created_by = models.CharField(max_length=50) 
    created_on  = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(max_length=50) 
    updated_on = models.DateTimeField(blank=True, null=True)
    def __str__(self):
       return self.id
