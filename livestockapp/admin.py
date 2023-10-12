from django.contrib import admin
from .models import AnimalProfile

# Register your models here.
@admin.register(AnimalProfile)
class AnimalProfile(admin.ModelAdmin):
    list_display = (
        'animal_id' ,
        'token_no' ,
        'name' ,
        'color' ,
        'weight' ,
        'image' ,
        'purchase_price' ,
        'purchased_on' ,
        'date_of_birth' ,
        'description',
        'gender',
        'status' 
    
    )