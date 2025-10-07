from django.urls import path

from . import views

from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
    
#     path('dresses/', views.dress_list_all, name='dress_list_all'),
#     path('laces/', views.lace_list_all, name='lace_list_all'),
    
#     path('dress/<int:id>/', views.dress_detail, name='dress_detail'),
#     path('add/', views.add_dress, name='add_dress'),
    
#     path('laces/', views.lace_list, name='lace_list'),
#     path('lace/<int:id>/', views.lace_detail, name='lace_detail'),
#     path('lace/add/', views.add_lace, name='add_lace'),
    
    
    
# ]


urlpatterns = [
    path('', views.home, name='home'),
    path('dresses/', views.dress_list_all, name='dress_list_all'),
    path('laces/', views.lace_list_all, name='lace_list_all'),
    path('dress/<int:id>/', views.dress_detail, name='dress_detail'),
    path('lace/<int:id>/', views.lace_detail, name='lace_detail'),
    path('admin/dress/add/', views.add_dress, name='add_dress'),
    path('admin/lace/add/', views.add_lace, name='add_lace'),
]