from django.urls import path

from . import views

from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('charge/', views.charge, name='charge'),
]