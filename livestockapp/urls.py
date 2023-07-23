from django.contrib import admin
from django.urls import path
from livestockapp import views
urlpatterns = [
    path('', views.cat_insert, name='insert'),
    path('show/', views.cat_show, name='show' ),
    path('delete/<int:category_id>/', views.cat_delete, name="delete"),
    path('edit/<int:category_id>/', views.cat_edit, name="edit"),
    path('update/<int:category_id>', views.cat_updated, name='update')
]