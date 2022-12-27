from django.urls import path

from .views import (
    NewsListView,
    NewsDetailView,
    RedactorDetailView,
    NewsCreateView,
    NewsUpdateView,
)


urlpatterns = [
    path("", NewsListView.as_view(), name="news-list"),
    path("news/<int:pk>/",
         NewsDetailView.as_view(),
         name="news-detail"),
    path(
        "redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path(
        "user/<int:pk>/", RedactorDetailView.as_view(), name="user-detail"
    ),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),
    path(
        "news/<int:pk>/update/",
        NewsUpdateView.as_view(),
        name="news-update",
    ),
]

app_name = "portal"
