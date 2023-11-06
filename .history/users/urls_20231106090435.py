from django.urls import path 
from . import views
app_name = 'users'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logut', views.log_out, name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]