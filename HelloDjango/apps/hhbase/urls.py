from django.urls import path
from . import views

urlpatterns = [
    path('add_hh_request/', views.AddRequestView.as_view(), name='hh_add_request'),
]