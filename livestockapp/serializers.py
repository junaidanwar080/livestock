from rest_framework import serializers
from .models import Animal_profile


class AnimalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_profile
        fields = ['animal_id','token_no','color','purchase_price','purchased_on','date_of_birth','description','gender','start_date','end_date','status','created_by','created_on','updated_by','updated_on']