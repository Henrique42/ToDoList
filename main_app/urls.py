from django.urls import path 
from main_app import views

urlpatterns = [
    path('', views.create_item, name='create_item'),  
    path('delete/<int:id>/', views.delete_item, name="delete"),
]