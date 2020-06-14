from django.urls import path

from users.views import (
    LoginView,
    LogoutView,
    SignupView,
    UpdateProfileView,
    UserDetailView,
)

app_name = 'users'

urlpatterns =[
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('signup',SignupView.as_view(),name='signup'),
    path('me/profile',UpdateProfileView.as_view(),name='update_profile'),
    # User Posts
    path('<str:username>/',view = UserDetailView.as_view(),name='detail'),
]