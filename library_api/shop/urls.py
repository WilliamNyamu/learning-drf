from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"gift", views.GiftAPIView)
router.register(r"merchandise", views.MerchandiseAPIView)


urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index")
]