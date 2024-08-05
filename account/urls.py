# from django.urls import path

# urlpatterns = [
#     # Post views
#     path('login/', views.user_login, name='login'),
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', views.logout_then_login, name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),
]