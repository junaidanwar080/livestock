from django.contrib import admin
from django.urls import path
from livestockapp import views
urlpatterns = [
#category
    path('', views.cat_insert, name='insert'),
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
    path('insert_pregnency_detail', views.insert_pregnency_detail , name='insert_pregnency_detail'),
    path('list_pregnency_detail/', views.list_pregnency_detail, name='list_pregnency_detail' ),
    path('animal_det_delete/<int:Pregnancy_id>/', views.animal_det_delete, name="animal_det_delete"),
    path('animal_det_edit/<int:Pregnancy_id>/', views.animal_det_edit, name="animal_det_edit"),
    path('update_pregnency_detail/<int:Pregnancy_id>', views.update_pregnency_detail, name='update_pregnency_detail')
]