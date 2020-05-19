from django.urls import path
from second_app import views

app_name = 'second_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('form/', views.form_name_view, name='form_name_view'),
    path('relative/', views.relative, name='relative'),
    path('registration/', views.registration, name = 'registration'),
    path('user_login/', views.user_login, name='user_login'),
     path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name = 'special'),
        
   
    
]