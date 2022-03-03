from django.urls import path

from users.views import login, registration, logout, profile, email_verification

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),  # ../users/login/
    path('registration/', registration, name='registration'),  # ../users/registration/
    path('logout/', logout, name='logout'),  # ../users/logout/
    path('profile/', profile, name='profile'),  # ../users/profile/
    path('verify/<str:email>/<uuid:code>/', email_verification, name='email_verification'),
    # ../verify/ivan@mail.com/50763334-c965-4f0b-ad2a-62f01ef2d692/
]
