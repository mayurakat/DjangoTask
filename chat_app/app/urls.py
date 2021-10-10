from django.db.models import fields
from app import models
from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
   
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('edit/',views.edit,name='edit'), 
    path('delete/',views.delete,name='delete'),     
    path('profile/',views.profile,name='profile'), 
    


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]