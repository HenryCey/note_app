from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogOutInterfaceView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
