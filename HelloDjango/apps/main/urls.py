from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainInfoView.as_view(), name='main'),
]