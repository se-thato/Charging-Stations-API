from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)

from .views import ProtectedView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('obtain_token/', TokenObtainPairView.as_view(), name= "obtain_token"),
    path('verify_token/', TokenVerifyView.as_view(), name="verify_token"),
    path('refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),

    path('protected-view/', ProtectedView.as_view(), name="protected-view"),


    # JWT authentication endpoints
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    #Session login/logout 
    path('api/auth/', include('rest_framework.urls')),
]
