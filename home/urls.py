from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('news',views.news,name='news'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('register',views.register,name='register')

]
