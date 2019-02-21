from django.urls import path,include

from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('recruiter_register/', views.registering),
    path('recruiter_login/',views.logining),
    path('', views.show),
    path('createjob/', views.createjob),
    path('registeringjob/', views.registeringjob),
    path('selectcandidate/<Job_id>', views.selectcandidate),
    path('deletejob/<Job_id>', views.deletejob),
    path('logout/', views.logout),
    path('shortlist/<Job_seeker_mail>/<Job_id>', views.shortlist)
]