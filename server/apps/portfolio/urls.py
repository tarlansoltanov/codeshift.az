from django.urls import path

from server.apps.portfolio.views import CategoryView, PortfolioView, ProjectView

app_name = "portfolio"

urlpatterns = [
    path("", PortfolioView.as_view(), name="portfolio"),
    path("<int:pk>/", ProjectView.as_view(), name="project"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
]
