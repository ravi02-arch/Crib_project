from django.urls import path
from . import views

urlpatterns = [
    path('view', views.view, name='item-views'),
    path('create', views.create, name='create-items'),
    path('update/<str:item_name>', views.update, name='update-items'),
    path('delete/<str:item_name>', views.delete, name='delete-items')
]