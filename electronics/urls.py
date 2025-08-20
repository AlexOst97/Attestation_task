from electronics.apps import ElectronicsConfig
from rest_framework.routers import DefaultRouter
from electronics.views import NetworkViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r"network", NetworkViewSet, basename="network")

app_name = ElectronicsConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(
            permission_classes=[
                AllowAny,
            ]
        ),
        name="login",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(
            permission_classes=[
                AllowAny,
            ]
        ),
        name="refresh",
    ),
]

urlpatterns += router.urls
