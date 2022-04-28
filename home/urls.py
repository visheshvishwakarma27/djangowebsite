from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('news',views.news,name='news'),
    path('contact',views.Contact,name='Contact'),
    path('services',views.services,name='services'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('forget',views.forget,name='forget')
   

]
