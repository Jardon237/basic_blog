from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='my_app-home'),
    path('about/', views.about, name='my_app-about')
   
]