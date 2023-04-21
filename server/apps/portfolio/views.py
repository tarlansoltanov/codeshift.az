from django.shortcuts import render


def index(request, template_name='portfolio/index.html', context={}):
    context['title'] = "Portfolio"
    context['selected'] = int(request.GET.get('category', 0))
    return render(request, template_name, context)


def project(request, template_name='portfolio/project.html', context={}):
    context['title'] = "Project Details"
    return render(request, template_name, context)