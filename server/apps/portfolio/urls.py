from django.urls import path

from server.apps.portfolio.views import PortfolioView, ProjectView

app_name = "portfolio"

urlpatterns = [
    path("", PortfolioView.as_view(), name="portfolio"),
    path("<int:pk>/", ProjectView.as_view(), name="project"),
]
