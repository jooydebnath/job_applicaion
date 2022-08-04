from django.urls import path
from . import views

urlpatterns = [
    path('', views.corporateDashboard, name='corporate-dashboard'),
    path('settings/', views.corporateProfile, name='settings'),
]