from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registraion_option/', views.registerPre, name='registraion_option'),
    path('corporate_register/', views.corporateRegister, name='corporate_register'),
    path('select-category/', views.selectCategory, name='select-category'),

    path('login/', views.login, name='login')
]