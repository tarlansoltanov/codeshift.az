from django.shortcuts import render
from .models import Project


def index(request, template_name='portfolio/index.html', context={}):
    context['title'] = "Portfolio"
    context['selected'] = int(request.GET.get('category', 0))

    context['projects'] = Project.objects.all().order_by('-created_at')

    return render(request, template_name, context)


def project(request, pk, template_name='portfolio/project.html', context={}):
    context['title'] = "Project Details"

    context['project'] = Project.objects.get(pk=pk)

    return render(request, template_name, context)