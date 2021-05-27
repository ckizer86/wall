from django.urls import path
from . import views
app_name='login_app'

urlpatterns = [
    path('', views.index, name="login_index"),
    path('success', views.success, name="login_success"),
    path('register', views.register, name="login_register"),
    path('login', views.login, name="login_login"),
    path('logout', views.logout, name="login_logout"),
]