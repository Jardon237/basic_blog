from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='my_app-home'),
    #path('<slug:post>/', views.detail, name='detail'),
    path('about/', views.about, name='my_app-about')
   
]