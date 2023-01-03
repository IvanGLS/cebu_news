import django
from django.urls import path

from .views import (
    comment_remove,
    errorhandler404,
    NewsListView,
    NewsDetailView,
    RedactorDetailView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
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
    path(
        "news/<int:pk>/delete/",
        NewsDeleteView.as_view(),
        name="news-delete",
    ),
    path(
        "comment/<int:pk>/remove/",
        comment_remove,
        name="comment-remove",
    ),
    path("404/", errorhandler404),
]

app_name = "portal"
