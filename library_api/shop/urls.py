from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"gift", views.GiftAPIView)
router.register(r"merchandise", views.MerchandiseAPIView)


urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("api-auth/", include("rest_framework.urls")),
    # path("api-token/", obtain_auth_token, name="obtain_auth_token")
]