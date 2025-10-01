from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", views.PostAPIView, basename="posts")

urlpatterns = [
    path("", include(router.urls))
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]