# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('upload/', views.upload_flower, name='upload_flower'),
#     path('flowers/', views.flower_list, name='flower_list'),
#     path('flower/<int:flower_id>/result/', views.result, name='result')


# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload_flower, name='upload_flower'),  # Upload flower page
    path('flowers/', views.flower_list, name='flower_list'),  # Flower list page
    path('result/', views.result_page, name='result_page'),
    
  # Flower prediction result
    
]
