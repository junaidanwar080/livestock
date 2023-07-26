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
    path('animal_pro_delete/<int:id>/', views.animal_pro_delete, name="animal_pro_delete"),
    path('animal_pro_edit/<int:id>/', views.animal_pro_edit, name="animal_pro_edit"),
    path('update_animal/<int:id>', views.update_animal, name='update_animal')
]