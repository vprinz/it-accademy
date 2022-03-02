from django.urls import path

from users.views import login, registration, logout, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),  # ../users/login/
    path('registration/', registration, name='registration'),  # ../users/registration/
    path('logout/', logout, name='logout'),  # ../users/logout/
    path('profile/', profile, name='profile'),  # ../users/profile/
]
