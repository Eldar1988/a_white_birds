from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainInfoView.as_view(), name='main'),
    path('contacts/', views.ContactView.as_view(), name='main_contacts'),
]