
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('list/', views.shopped_items,name = 'shopped_items'),
    path('products/', views.list_product,name ='list_product'),
    path('add_product/', views.add_product,name ='add_product'),
    path('update_product/<int:pid>', views.update_product,name ='update_product'),
    path('delete_product/<int:pid>', views.delete_product,name ='delete_product'),
    path('list_category/', views.list_category,name = 'list_category'),
    path('delete_category/<int:pid>', views.delete_category,name ='delete_category'),
]