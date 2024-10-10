from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from accounts.views import RegisterView


urlpatterns = [
    path('login/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
