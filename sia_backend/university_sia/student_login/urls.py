# student_login/urls.py
from django.urls import path
from .views import LoginView, RegisterUserView

urlpatterns = [
    path('/login/', LoginView.as_view(), name='login'),  # Para el login
    path('/register/', RegisterUserView.as_view(), name='register'),  # Para el registro
]
