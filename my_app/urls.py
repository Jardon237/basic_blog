from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('<slug:post>/', views.detail, name='detail'),
   
]