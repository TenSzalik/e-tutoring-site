from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers
from tutorial.urls import router as tutorial
from user_profile.urls import router as user_profile


router = routers.DefaultRouter()

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/tutorial/", include(tutorial.urls)),
    path("api/user_profile/", include(user_profile.urls)),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
