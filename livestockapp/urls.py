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
    path('insert_pregnancy_detail', views.insert_pregnancy_detail , name='insert_pregnancy_detail'),
    path('list_pregnancy_detail/', views.list_pregnancy_detail, name='list_pregnancy_detail' ),
    path('pregnancy_det_delete/<int:pregnancy_id>/', views.pregnancy_det_delete, name="pregnancy_det_delete"),
    path('pregnancy_det_edit/<int:pregnancy_id>/', views.pregnancy_det_edit, name="pregnancy_det_edit"),
    path('update_pregnancy_detail/<int:pregnancy_id>', views.update_pregnancy_detail, name='update_pregnancy_detail'),
   # path('list_of_animals', views.table_join)
]