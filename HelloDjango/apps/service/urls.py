from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name="service_list"),
    path('detail/<int:pk>', views.SubServiceDetail.as_view(), name="subservice_detail"),
    path('<int:pk>/', views.ServiceDetail.as_view(), name="service_detail"),
    path('new_resume', views.AddNewResume.as_view(), name="add_resume"),
    path('add_contact_service', views.AddContactRequest.as_view(), name="add_contact_service"),
]