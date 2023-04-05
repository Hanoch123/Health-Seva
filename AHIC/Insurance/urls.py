from django.urls import path

from . import views

urlpatterns = [
    path('inshome/', views.InsureHome, name="inshome"),
    path('inslogin/', views.InsureLogin, name="inslogin"),
    path('insregister/', views.InsureRegister, name="insregister"),
    path('insprofile/', views.InsureProfile, name="insprofile"),
    path('insplans/', views.InsurePlans, name="insplans"),
    path('inspolicy/', views.InsurePolicy, name="inspolicy"),
    path('inslogout/', views.InsureLogout, name="inslogout"),
    path('insclients/', views.InsureClients, name="insclients"),
    path('insclaims/', views.InsureClaims, name="insclaims"),
    path('client_details/<str:cl_no>/', views.InsureCliDetails, name="client_details"),
    path('claim_dets/<str:dets_no>/', views.InsureClaimDetails, name="claim_dets"),
]