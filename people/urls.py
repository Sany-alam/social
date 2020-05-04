from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.peoples,name="peoples"),
    path('show',views.showpeoples,name="showpeoples")
]