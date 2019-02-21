from django.contrib import admin  
from django.urls import path,include
  
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.url')), 
    path('user/', include('user.url')),
    path('recruiter/', include('recruiter.url'))
]  