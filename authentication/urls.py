from django.urls import path
from authentication.views import login,register,logout, get_user

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('user/', get_user, name='get_user'),
]
