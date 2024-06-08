from django.urls import path
from app.views import *

urlpatterns = [
	path("",index,name="main_page"),
    path("auth/login",auth_login,name="auth_login"),
    path("auth/register",auth_register,name="auth_register"),
    path("auth/logout",auth_logout,name="auth_logout")
]
