from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Commented out previous login view
    # path('login/', views.user_login, name='login'),

    # Login / logout URLs
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', views.logout_then_login, name='logout_then_login'),
]
