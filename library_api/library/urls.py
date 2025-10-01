from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r"",views.ReviewAPIView)

urlpatterns = [
    path("review/", include(router.urls)),
    path("authors/", views.AuthorListAPIView.as_view(), name="author_list"),
    path("books/test/", views.BookListAPIView.as_view(), ),
    path("books/", views.BookCreateListAPIView.as_view()),
    path("books/<int:pk>/", views.RetrieveAndUpdateAndDestroyAPIView.as_view()),
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls"))
]