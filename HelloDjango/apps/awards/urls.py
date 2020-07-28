from django.urls import path
from . import views

urlpatterns = [
    path('add_jury_approved/<int:pk>', views.AddJuryApprovedView.as_view(), name="add_jury_approved"),
    path('', views.AwardView.as_view(), name='award'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('add_request/', views.AddRequestView.as_view(), name='add_request'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('award_request/<int:pk>', views.RequestDetailView.as_view(), name="request_detail"),
    path('award_detail/', views.AwardDetailView.as_view(), name="award_detail"),
    path('add_vote/<int:pk>', views.AddVoteView.as_view(), name="add_vote"),
    path('request_detail/<int:pk>', views.RequestSelfDetailView.as_view(), name="self_detail"),
]