from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.Index, name="index"),
    path('home/', views.Home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('insurance/', views.Insurance, name="insurance"),
    path('myplans/', views.MyPlans, name="myplans"),
    path('claim/', views.Claims, name="claim"),
    path('new_claim/', views.NewClaim, name="new_claim"),
    path('wallet/', views.CliWallet, name="wallet"),
    path('claim_details/<str:bil_no>',views.ClaimDetails, name="claim_details"),
    path('notifications/<str:not_no>/', views.CliNotify, name="notifications"),
    path('ins_policy/<str:bk_no>/', views.InsDetails, name="ins_policy"),
]