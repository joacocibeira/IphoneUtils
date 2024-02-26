from django.urls import path
from register.api.api import RegisterView, LoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login')
]