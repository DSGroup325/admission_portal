from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission_form, name='admission_form'),
    path('success/', views.success, name='success'),
    path('pdf/<int:pk>/', views.admission_pdf, name='admission_pdf'),
]