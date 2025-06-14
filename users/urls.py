from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path("register/", UserListCreateView.as_view(), name="user-register"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]