from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('sales/', views.sales, name='sales'),
    path('purchase/', views.purchase, name='purchase'),
    
]
