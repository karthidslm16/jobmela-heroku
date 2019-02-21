from django.urls import path,include

from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('user_register/', views.registering),
    path('user_login/', views.logining),
    path('search/',views.search),
    path('apply/<Job_id>',views.apply),
    path('', views.show),
    path('logout/', views.logout)
]