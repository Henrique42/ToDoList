from django.urls import path 
from main_app import views

urlpatterns = [
    path('', views.create_item, name='create_item'),  
    path('delete', views.delete_item, name="delete"),
    path('update-item', views.update_item, name='update-item'),
    path('update-status', views.update_status, name='update-status')
]