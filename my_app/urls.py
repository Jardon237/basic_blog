from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('<slug:slug>/', views.detail, name='post_detail'),
    path('new_post/',views.new_post, name='new_post')
]