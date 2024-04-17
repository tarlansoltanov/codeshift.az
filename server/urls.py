"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from server.apps.base import urls as base_urls
from server.apps.portfolio import urls as portfolio_urls

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include(base_urls, namespace="base")),
    path("portfolio/", include(portfolio_urls, namespace="portfolio")),
)

urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
]

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [path("translations/", include("rosetta.urls"))]

# Django Health Check
urlpatterns += [
    path("health/", include("health_check.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # noqa: WPS433

    # Django Debug Toolbar
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    # Serving media files in development only:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
