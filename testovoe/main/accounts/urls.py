from django.urls import path,include
from .views import registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/', registration),
    path('autorithation', auth_views.LoginView.as_view(), name='login')
]