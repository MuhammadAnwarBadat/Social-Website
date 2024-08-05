from django.urls import path
from . import views

urlpatterns = [
    # Post views
    path('login/', views.user_login, name='login'),
]