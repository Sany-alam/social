from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('register/',views.register,name="register"),
    path('profile/<str:username>',views.profile,name="profile"),
    path('profile/',views.profile,name="profile"),


    path('ValidUsername/',views.ValidUsername,name="ValidUsername"),
    path('Validemail/',views.Validemail,name="Validemail"),
]
