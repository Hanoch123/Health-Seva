from django.urls import path

from . import views

urlpatterns = [
    path('hospregister/', views.HospRegister, name="hospregister"),
    path('hosplogin/', views.HospLogin, name="hosplogin"),
    path('hosphome/', views.HospHome, name="hosphome"),
    path('hosplogout/', views.HospLogout, name="hosplogout"),
    path('hospappr/', views.ClaimAppr, name="hospappr"),
    path('hospclaim/', views.HospClaims, name="hospclaim"),
    path('hospnewclaim/', views.HospNewClaim, name="hospnewclaim"),
    path('hospnotifs/', views.HospNotifs, name="hospnotifs"),
    path('hospwallet/', views.HospWallet, name="hospwallet"),
    path('hospapproval/<str:appr_no>/', views.HospApproval, name="hospapproval"),
]