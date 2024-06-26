from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils import translation
from django.views.generic import RedirectView, TemplateView

from server.apps.base.logic.forms import MessageForm
from server.apps.portfolio.models import Project


class IndexView(RedirectView):
    """Index view."""

    def get_redirect_url(self, *args, **kwargs):
        translation.activate("az")
        return reverse("base:home")


class HomeView(TemplateView):
    """Home view."""

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Home"

        context["projects"] = Project.objects.all().order_by("-modified_at")[:4]

        return context


class AboutView(TemplateView):
    """About view."""

    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "About"

        return context


class ContactView(TemplateView):
    """Contact view."""

    template_name = "base/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact"

        context["form"] = MessageForm()

        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)

        if form.is_valid() and request.accepts("application/json"):
            form.save()

            return HttpResponse("Message sent successfully")

        return HttpResponse("Please fill all the fields correctly!", status=400)
