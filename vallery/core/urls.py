from django.urls import path
from django.views.decorators.cache import cache_page

from vallery.core.views import (
    AboutPage,
    BlogDetailPage,
    BlogPage,
    ContactPage,
    HomePage,
    SupportPage,
)

app_name = "core"

urlpatterns = [
    path("", cache_page(60 * 15)(HomePage.as_view()), name="home"),
    path("about/", cache_page(60 * 15)(AboutPage.as_view()), name="about"),
    path("contact/", cache_page(60 * 15)(ContactPage.as_view()), name="contact"),
    path("blog/", cache_page(60 * 15)(BlogPage.as_view()), name="blog"),
    path(
        "blog/<str:slug>/",
        cache_page(60 * 15)(BlogDetailPage.as_view()),
        name="blog_detail",
    ),
    path("support/", cache_page(60 * 15)(SupportPage.as_view()), name="support"),
]
