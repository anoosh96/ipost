

from django.contrib.auth.urls import urlpatterns 
from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from . import views

app_name="users"

urlpatterns=[
    path('register/',views.UserRegisterView.as_view(),name="register"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',views.UserLogoutView.as_view(),name="logout"),
    path('',views.UserRegisterView.as_view(),name="store"),
    path('<int:pk>/',views.UserProfile.as_view(),name="detail"),
    path('relation/',views.UserRelation.as_view(),name="followUnfollow")
]