from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidateDashboard, name='candidate-dashboard'),
    path('special-category-dashboard/', views.specialCategory, name='candidate-dashboard'),
    path('disabled-categorys-dashboard/', views.autismCategory, name='candidate-dashboard'),
]