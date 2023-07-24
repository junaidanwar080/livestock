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
    path('insert_animal_profile/', views.animal_pro_insert),
    path('list_animal_profile/', views.animal_pro_show, name='list_animal_profile' ),
    path('delete/<int:id>/', views.animal_pro_delete, name="delete"),
    path('edit/<int:id>/', views.animal_pro_edit, name="edit"),
    path('update/<int:id>', views.animal_pro_updated, name='update')
]