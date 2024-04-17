from django.views.generic import TemplateView

from .models import Project


class PortfolioView(TemplateView):
    """Portfolio view."""
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Portfolio"

        context["projects"] = Project.objects.all().order_by("-modified_at")

        return context


class ProjectView(TemplateView):
    """Project view."""

    template_name = "portfolio/project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Project Details"

        context["project"] = Project.objects.get(pk=kwargs["pk"])

        return context
