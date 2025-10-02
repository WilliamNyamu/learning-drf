from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", views.PostAPIView, basename="posts")
router.register(r"users", views.UserAPIView, basename="users")
router.register(r"comments", views.CommentAPIView, basename="comments")

urlpatterns = [
    path("test/", include(router.urls))
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]